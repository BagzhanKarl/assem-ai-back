import json
from openai import OpenAI

import crud
import main
import whatsapp

def generate_ai(key, messages):
    client = OpenAI(api_key=key)

    functions = [
        {
            "name": "add_user_on_black_list",
            "description": "Добавляет пользователя на черный список Whatsapp навсегда через номер телефона.",
            "parameters": {
                "type": "object",
                "properties": {
                    "number": {
                        "type": "string",
                        "description": "Номер телефона пользователя который надо добавить на черный список. Например, ChatID: 77761174378@40.whatsapp.net. А номер получается: 77761174378",
                    },
                },
                "required": ["number"],
                "additionalProperties": False,
            },
        },
        {
            "name": "create_meet_on_top_manager",
            "description": "Создает запись о встрече с топ менеджером проекта чтобы поговорить о сотрудничесве",
            "parameters": {
                "type": "object",
                "properties": {
                    "chat_id": {
                        "type": "string",
                        "description": "ID чата пользователя который вы общаетесь, например, 77761174378@40.whatsapp.net",
                    },
                    "name": {
                        "type": "string",
                        "description": "Имя пользователя который вы общаетесь, например, Багжан",
                    },
                    "date": {
                        "type": "string",
                        "description": "Дата встречи, например, 08.10.2024",
                    },
                    "time": {
                        "type": "string",
                        "description": "Время встечи, напримет, 10:00",
                    },
                    "user_data": {
                        "type": "string",
                        "description": "Короткая но подробная информация чтобы перед встречи топ менеджер мог прочитать и знал о клиенте",
                    },
                },
                "required": ["chat_id", "name", "date", "time", "user_data"],
                "additionalProperties": False,
            },
        }
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        functions=functions,
        function_call="auto",
    )

    response_message = completion.choices[0].message
    if response_message.function_call:

        function_name = response_message.function_call.name
        function_args = json.loads(response_message.function_call.arguments)

        if function_name == "add_user_on_black_list":
            function_response = whatsapp.add_user_on_black_list(**function_args)

            return 'Пользователь заблокирован'

        if function_name == "create_meet_on_top_manager":
            function_response = main.create_meet_on_top_manager(**function_args)

            return 'Встреча создан'
    else:
        return response_message.content