# import datetime
# import time

'''
Полезная работа с модулем datetime,
'''
# d = datetime.date(2024, 11, 17)
# print(d)
# t = datetime.time(14, 30, 45)
# print(t)
# dt = datetime.datetime(2024, 11, 17, 11,14,30)
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))
# ts = time.time()
# dt = datetime.datetime.fromtimestamp(ts).strftime('%d.%m.%Y %H:%M:%S')
# print(dt)

'''
GET - запрос от сервера, когда мы хотим получить информацию 
о некотором пользователе и сервер возвращает информацию

POST - запрос на добавление какой-либо новой информации на сервер
мы отправляем новую информацию и на её основе хотим получить
какой-либо короткий ответ, либо чтобы сервер принял какие-либо действия

Простейшая API от сбера, которая предоставляет доступ к простейшей языковой модели
годится только на то, чтобы поддержать простую беседу

'''

import requests

url = 'https://api.aicloud.sbercloud.ru/public/v2/boltalka/predict'

context = []

def get_response(text):
    context.append(text)
    data = {
        'instances': [
            {
                'contexts': [
                    context
                ]
            }
        ]
    }
    response = requests.post(url, json=data)
    return response.json()['responses'].split("'")[1].replace('%bot_name', 'Лада')



if __name__ == "__main__":
    while True:
        text = input('Пользователь: ')
        print('Бот: ' + get_response(text))







