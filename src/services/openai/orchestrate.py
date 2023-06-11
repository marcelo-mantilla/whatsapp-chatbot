from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from src.services.chat.create import create_message
from models import UserModel
from models import ChatModel

import os


def orchestrate_response(user: UserModel, chat: list[ChatModel]):
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    chat_openai = ChatOpenAI(temperature=0.8, model_name='gpt-3.5-turbo', max_tokens=500)

    chat.sort(key=lambda x: x.created_at)
    langchain_history = compose_langchain_history(chat)

    print('LANGCHAIN HISTORY', langchain_history)

    # langchain ...

    # gpt_response = {'message': '...'}
    # gpt_message = create_message(
    #     user=user,
    #     message=gpt_response['message'],
    #     category='TEXT',
    #     origin='LLM',
    # )
    # chat.append(gpt_message)
    # return gpt_message


def compose_langchain_history(chat: list[ChatModel]):
    history = []
    for message in chat:
        match message.category:
            case 'TEXT':
                history.append(HumanMessage(content=message.message))
            case 'LLM':
                history.append(AIMessage(content=message.message))
            case 'SYSTEM':
                history.append(SystemMessage(content=message.message))

    return history
