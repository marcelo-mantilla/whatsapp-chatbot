import json
import os
import requests


def create_whatsapp_request(phone_number: str, text: str, recipient_type: str = 'individual'):
    try:
        url = os.getenv('WHATSAPP_MESSAGES_URL')
        headers = {
            'Authorization': 'Bearer ' + os.getenv('WHATSAPP_ACCESS_TOKEN'),
            'Content-Type': 'application/json'
        }
        body = json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": phone_number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": text
            }
        })
        response = requests.post(url, headers=headers, data=body)
        print(response.json())
        return response

    except Exception as e:
        print(e)
