"""
Standard WhatsApp webhooks payload:
https://developers.facebook.com/docs/whatsapp/cloud-api/guides/set-up-webhooks

{
  "object": "whatsapp_business_account",
  "entry": [{
      "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
      "changes": [{
          "value": {
              "messaging_product": "whatsapp",
              "metadata": {
                  "display_phone_number": "PHONE_NUMBER",
                  "phone_number_id": "PHONE_NUMBER_ID"
              },
              # specific Webhooks payload
          },
          "field": "messages"
        }]
    }]
}
"""


def process_whatsapp_entry(entries: list) -> dict:
    processed_entries = []
    for entry in entries:
        for change in entry['changes']:
            value = change['value']
            metadata = get_metadata(value['metadata'])
            contacts = get_contacts(value['contacts'])
            messages = get_messages(value['messages'])
            processed_entries.append({
                **metadata,
                'name': contacts[0]['name'],
                'contacts': contacts,
                'messages': messages,
            })

    if len(processed_entries) > 1:
        # log
        print(f'MULTIPLE ENTRIES RECEIVED: {processed_entries}')
    if len(contacts) > 1:
        # log
        print(f'MULTIPLE CONTACTS RECEIVED: {contacts}')

    return processed_entries[0]


def get_contacts(contacts: list):
    contact_list = []
    for contact in contacts:
        contact_list.append({
            'name': contact['profile']['name'],
            'phone_number': contact['wa_id']
        })
    return contact_list

def get_metadata(metadata: dict):
    return {
        'phone_number': metadata['display_phone_number'],
        'phone_number_id': metadata['phone_number_id']
    }

def get_messages(messages: list[dict]):
    responses = []
    for message in messages:
        phone_number = message['from']
        whatsapp_id = message['id']
        timestamp = message['timestamp']
        message_type = message['type']

        text, reaction = None, None

        if message_type == 'text':
            text = message['text']['body']
        elif message_type == 'reaction':
            reaction = message['reaction']['emoji']

        responses.append({
            'phone_number': phone_number,
            'whatsapp_id': whatsapp_id,
            'timestamp': timestamp,
            'type': message_type,
            'text': text,
            'reaction': reaction,
        })

    return responses
