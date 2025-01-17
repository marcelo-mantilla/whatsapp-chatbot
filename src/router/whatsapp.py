import os

from flask import request, Blueprint

from src.services.whatsapp.request import create_whatsapp_request
from src.services.whatsapp.webhook_payload import process_whatsapp_entry
from src.services.user.get_or_create import get_or_create_user
from src.services.chat.initialize import get_or_initialize_chat
from src.services.openai.orchestrate import orchestrate_response
from src.services.chat.create import save_message

whatsapp = Blueprint('whatsapp', __name__, url_prefix='/whatsapp')


@whatsapp.route('/webhooks', methods=['POST'], endpoint='receive_webhook')
def receive_webhook():
    # validate from facebook
    try:
        request_data = request.get_json()
        data = process_whatsapp_entry(request_data['entry'])
        user = get_or_create_user(data['name'], data['contacts'][0]['phone_number'])
        chat = get_or_initialize_chat(user)
        message = save_message(
            user=user,
            message=data['messages'][0]['text'],
            category=data['messages'][0]['type'],
            origin='USER',
            wa_created_at=data['messages'][0]['timestamp']
        )
        chat.append(message)
        openai_response: str = orchestrate_response(chat=chat)
        save_message(
            user=user,
            message=openai_response,
            category='TEXT',
            origin='LLM',
        )
        create_whatsapp_request(user.phone_number, openai_response)
        return 200

    except Exception as e:
        print('Internal Server Error', e)
        return 'Internal Server Error', 500


# Verification
@whatsapp.route('/webhooks', methods=['GET'], endpoint='verify_webhook')
def verify_webhook():
    hub_mode = request.args.get('hub.mode')
    hub_challenge = request.args.get('hub.challenge')
    verify_token = request.args.get('hub.verify_token')

    if hub_mode == 'subscribe' and verify_token == os.getenv('WHATSAPP_VERIFY_TOKEN'):
        return hub_challenge

    return 'Bad Request', 400
