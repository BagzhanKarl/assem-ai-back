import requests

def sent_text_message(text, chat_id, token):
    url = "https://gate.whapi.cloud/messages/text"
    payload = {
        "typing_time": 0,
        "body": text,
        "to": chat_id,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

def add_user_on_black_list(number):
    url = f"https://gate.whapi.cloud/blacklist/{number}"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer THjJOt2vo26nYYj4IbqKXVqInFv1wx55"
    }

    response = requests.put(url, headers=headers)
    return response.text