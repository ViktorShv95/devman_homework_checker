import os
import requests
from requests import exceptions
from dotenv import load_dotenv
import telegram


def main():

    load_dotenv()

    BASE_URL = 'https://dvmn.org/api/long_polling/'
    DEVMAN_TOKEN = os.environ['AUTH_TOKEN']
    BOT_TOKEN = os.environ['BOT_TOKEN']
    CHAT_ID = os.environ['CHAT_ID']
    HEADERS = {
    'Authorization': 'Token {}'.format(DEVMAN_TOKEN)
    }
    params = {}

    bot = telegram.Bot(token=BOT_TOKEN)
    
    while True:
        try:
            response = requests.get(BASE_URL, headers=HEADERS, params=params)
            response.raise_for_status()
            data = response.json()

            if data['status'] == 'found':
                params['timestamp'] = data['last_attempt_timestamp']
                new_attempt = data['new_attempts'][0]
                is_negative = new_attempt['is_negative']
                lesson_title = new_attempt['lesson_title']
                lesson_url = f'https://dvmn.org{new_attempt["lesson_url"]}'

                if is_negative:
                    bot.send_message(chat_id=CHAT_ID,
                                     text=f'Работа "{lesson_title}" проверена.\n'
                                     f'К сожалению, в работе были найдены ошибки.\n{lesson_url}')
                else:
                    bot.send_message(chat_id=CHAT_ID,
                                     text=f'Работа "{lesson_title}" проверена.\nПреподавателю всё понравилось!'
                                     f' Можно приступать к следующему заданию!\n{lesson_url}')

            elif data['status'] == 'timeout':
                params['timestamp'] = data['timestamp_to_request']

        except (exceptions.ReadTimeout, exceptions.ConnectionError) as error:
            bot.send_message(chat_id=CHAT_ID, text=f'Бот упал с ошибкой {error}')
            continue


if __name__ == '__main__':
    main()

  

