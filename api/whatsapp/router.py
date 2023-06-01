import json
import os

import requests
from flask import request, Blueprint

from api.whatsapp.compose_payload import text_response
from api.whatsapp.receive_payload import process_entries
from api.whatsapp.templates import introduction

whatsapp_router = Blueprint('whatsapp', __name__, url_prefix='/whatsapp')


@whatsapp_router.route('/webhooks', methods=['POST'], endpoint='receive_webhook')
def receive_webhook():
    try:
        request_data = request.get_json()

        # Eventual webhook orchestration layer will be needed
        # Check Meta webhook fields

        entries = request_data['entry']
        data = process_entries(entries)

        # OpenAI Logic

        body = text_response('19053275408', 'Hello, this is a test message.')
        url = os.getenv('WHATSAPP_MESSAGES_URL')
        headers = {
            'Authorization': 'Bearer ' + os.getenv('WHATSAPP_ACCESS_TOKEN'),
            'Content-Type': 'application/json'
        }
        print("Calling Meta API...")
        response = requests.post(url, headers=headers, data=body)
        print(f"META RESPONSE: {response.json()}")

        return 'ok'
    except Exception as e:
        print(e)
    finally:
        return 'ok'


# Verification
@whatsapp_router.route('/webhooks', methods=['GET'], endpoint='verify_webhook')
def verify_webhook():
    hub_mode = request.args.get('hub.mode')
    hub_challenge = request.args.get('hub.challenge')
    verify_token = request.args.get('hub.verify_token')

    if hub_mode == 'subscribe' and verify_token == os.getenv('WHATSAPP_VERIFY_TOKEN'):
        return hub_challenge

    return 'Bad Request', 400


@whatsapp_router.route('/initiate', methods=['POST'])
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
