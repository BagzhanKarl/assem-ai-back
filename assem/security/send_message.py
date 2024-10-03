import requests


def send_message(token, typing_time, to, body):
    url = "https://gate.whapi.cloud/messages/text"

    payload = {
        "typing_time": typing_time,
        "to": to,
        "body": body
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text