from flask import request, Blueprint
from langchain.chat_models import ChatOpenAI
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

from whatsapp.templates import introduction
from whatsapp.receive_payload import process_entries
import json
import requests
import os


whatsapp = Blueprint('whatsapp', __name__, url_prefix='/whatsapp')

@whatsapp.route('/initiate', methods=['POST'])
def post():
    request_data = request.get_json()
    phone_number = request_data['phone_number']

    url = os.getenv('WHATSAPP_MESSAGES_URL')
    headers = {
        'Authorization': 'Bearer ' + os.getenv('WHATSAPP_ACCESS_TOKEN'),
        'Content-Type': 'application/json'
    }
    body = json.dumps(introduction(phone_number))
    response = requests.post(url, headers=headers, data=body)
    print(response.json())
    return 'OK'


@whatsapp.route('/webhooks', methods=['POST'], endpoint='receive_webhook')
def receive_webhook():
    request_data = request.get_json()
    # Eventual llm_orchestration layer will be needed
    # Check Meta webhook fields

    entries = request_data['entry']
    data = process_entries(entries)

    print(f"DATA {data}")

    # OpenAI Logic


    return 'ok'


# Verification
@whatsapp.route('/webhooks', methods=['GET'], endpoint='verify_webhook')
def verify_webhook():
    hub_mode = request.args.get('hub.mode')
    hub_challenge = request.args.get('hub.challenge')
    verify_token = request.args.get('hub.verify_token')

    if hub_mode == 'subscribe' and verify_token == os.getenv('WHATSAPP_VERIFY_TOKEN'):
        return hub_challenge

    return 'Bad Request', 400
