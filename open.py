import json
from openai import OpenAI
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
    else:
        return response_message.content