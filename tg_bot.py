import telegram
import requests
import time
import os
from dotenv import load_dotenv


def check_task_status(token):
    url = "https://dvmn.org/api/long_polling/"
    headers = {
        "Authorization": f"Token {token}"
    }
    payloads = {
        "timestamp": ""
    }
    attempts_conn = 0
    while True:
        try:
            response = requests.get(url, params=payloads, timeout=500, headers=headers)
            response.raise_for_status()
            review_result = response.json()
            response_status = review_result["status"]
            if response_status == "found":
                lesson = review_result["new_attempts"][0]
                lesson_status = lesson["is_negative"]
                lesson_title = lesson["lesson_title"]
                lesson_url = lesson["lesson_url"]
                template = f"У вас проверели работу '{lesson_title}' \n{lesson_url}\n"
                if lesson_status:
                    message = f"{template}К сожалению, в работе нашлись ошибки"
                    return message
                else:
                    message = f"{template}Преподователю все понравилось, можно приступать к следующему уроку"
                    return message
            if response_status == "timeout":
                payloads = {"timestamp": review_result["timestamp_to_request"]}
            attempts_conn = 0
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            print("Are you connected to your internet?")
            attempts_conn += 1
            if attempts_conn == 1:
                continue
            else:
                time.sleep(10)


def main():
    load_dotenv()
    dvmn_token = os.environ['DVMN_TOKEN']
    tg_token = os.environ["TG_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    message = check_task_status(dvmn_token)
    bot = telegram.Bot(token=tg_token)
    bot.send_message(text=message, chat_id=chat_id)


if __name__ == '__main__':
    main()

