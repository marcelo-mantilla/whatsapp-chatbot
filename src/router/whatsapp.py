import json
import os

import requests
from flask import request, Blueprint

from src.services.whatsapp.request import create_request
from src.services.whatsapp.webhook_payload import process_whatsapp_entry
from src.services.whatsapp.templates import introduction
from src.services.user.get_or_create import get_or_create_user
from src.services.chat.initialize import get_or_initialize_chat
from src.services.openai.orchestrate import orchestrate_response
from src.services.chat.create import create_message

whatsapp = Blueprint('whatsapp', __name__, url_prefix='/whatsapp')


@whatsapp.route('/webhooks', methods=['POST'], endpoint='receive_webhook')
def receive_webhook():
    try:
        request_data = request.get_json()

        # Webhook Orchestration Layer

        data = process_whatsapp_entry(request_data['entry'])
        user = get_or_create_user(data['name'], data['phone_number'])
        chat = get_or_initialize_chat(user)
        message = create_message(
            user=user,
            message=data['messages'][0]['text'],
            category=data['messages'][0]['type'],
            origin='USER',
            wa_created_at=data['messages'][0]['timestamp']
        )
        chat.append(message)
        response = orchestrate_response(user=user, chat=chat)

        ### OpenAI Logic
        # 3. send to OpenAI
        # 4. parse response
        # 5. append to sequence
        # 5.5 save?
        # 6. send webhook with response

        body = create_request('19053275408', 'Hello, this is a test message.')
        url = os.getenv('WHATSAPP_MESSAGES_URL')
        headers = {
            'Authorization': 'Bearer ' + os.getenv('WHATSAPP_ACCESS_TOKEN'),
            'Content-Type': 'application/json'
        }
        print("Calling Meta API...")
        response = requests.post(url, headers=headers, data=body)
        print(f"META RESPONSE: {response.json()}")

        return '', 200
    except Exception as e:
        print(e)
    finally:
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


@whatsapp.route('/initiate', methods=['POST'])
def post():
    request_data = request.get_json()
    phone_number = request_data['phone_number']

    # get or create user

    url = os.getenv('WHATSAPP_MESSAGES_URL')
    headers = {
        'Authorization': 'Bearer ' + os.getenv('WHATSAPP_ACCESS_TOKEN'),
        'Content-Type': 'application/json'
    }
    body = json.dumps(introduction(phone_number))
    response = requests.post(url, headers=headers, data=body)
    print(response.json())
    return 'OK'
