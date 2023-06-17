from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from models import MessageModel
from models import OpenAILogModel
from src.services.openai.functions import create_calendar_event_function, get_events_list_function
from src.services.google.calendar import create_calendar_event
from src.services.google.events import get_calendar_events
import json
import os
from db import db


def orchestrate_response(chat: list[MessageModel]) -> str:
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    chat.sort(key=lambda x: x.created_at)
    langchain_history = _compose_langchain_history(chat)

    chat_openai = ChatOpenAI(temperature=0.8, model_name='gpt-3.5-turbo-0613', max_tokens=500)
    functions = [create_calendar_event_function(), get_events_list_function()]
    response = chat_openai.predict_messages(langchain_history, functions=functions)

    openai_log = OpenAILogModel(content=response.content, log=json.dumps(response.additional_kwargs))
    db.session.add(openai_log)
    db.session.commit()

    function_call = response.additional_kwargs['function_call']['name']
    arguments = json.loads(response.additional_kwargs['function_call']['arguments'])

    if function_call == 'create_calendar_event':
        # validate args
        create_calendar_event(arguments)
    elif function_call == 'get_events_list':
        # validate args
        get_calendar_events(arguments)

    return response.content


def _compose_langchain_history(chat: list[MessageModel]):
    history = []
    for message in chat:
        match message.origin:
            case 'USER':
                history.append(HumanMessage(content=message.message))
            case 'LLM':
                history.append(AIMessage(content=message.message))
            case 'SYSTEM':
                history.append(SystemMessage(content=message.message))

    return history
