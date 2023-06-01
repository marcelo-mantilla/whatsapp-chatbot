import json


def text_response(phone_number:str, text:str, recipient_type:str = 'individual'):
    response = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": recipient_type,
        "to": phone_number,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": text
        }
    })
    return response
