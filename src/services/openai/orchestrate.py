from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from models import MessageModel
import os


def orchestrate_response(chat: list[MessageModel]) -> str:
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    chat.sort(key=lambda x: x.created_at)
    langchain_history = compose_langchain_history(chat)

    chat_openai = ChatOpenAI(temperature=0.8, model_name='gpt-3.5-turbo', max_tokens=500)
    response = chat_openai.predict_messages(langchain_history)

    ### Google Calendar
    # - How do I orchestrate this?

    return response.content


def compose_langchain_history(chat: list[MessageModel]):
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
