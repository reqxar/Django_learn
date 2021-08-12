import requests


def sendMessage(token, chat_id, name, phone):
    api = 'https://api.telegram.org/bot'
    method = f"{api}{token}/sendMessage"

    text = f'Пользователь {name} оформил заявку\nСвязаться с ним можно по телефону: {phone}'

    req = requests.post(method, 
        data={
            'chat_id': chat_id,
            'text': text
        }
    )

    

