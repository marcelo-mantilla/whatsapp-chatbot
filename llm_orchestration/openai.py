from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

import os


def orchestrate_response(text: str, name: str):
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

    chat = ChatOpenAI(temperature=0.8, model_name='gpt-3.5-turbo', max_tokens=500)
    prompt = f"""
        The name of the person you are interacting with is called {name}. 
        You can ask them questions about themselves.
    """
    messages = [
        SystemMessage(content=prompt),
        *compose_message_history(),
        HumanMessage(content=text),
    ]
    ai_message = chat(messages)
    return ai_message


def compose_message_history() -> list[str]:
    return []
