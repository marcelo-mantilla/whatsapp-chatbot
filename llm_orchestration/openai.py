from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation import base
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def orchestrate_response(text:str, name:str) -> str:
    chat = ChatOpenAI(temperature=0.5)
    system_message = f"""
        Hello, I'm a bot. I'm here to help you learn English.
    """
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=text)
    ]
    ai_message = chat(messages)

    return ai_message
