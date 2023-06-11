import os


class WhatsAppTemplate:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        # self.individual
        # self.


def introduction(phone_number: str):
    return {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone_number,
        'type': 'template',
        'template': {
            'name': 'introduction',
            'language': {'code': 'en_US'}
        },
    }

# TODO
# preview
# what else ?
def text_response(phone_number: str):
    return {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone_number,
        'type': 'text',
        'template': {
            'name': 'introduction',
            'language': {'code': 'en_US'}
        },
    }


