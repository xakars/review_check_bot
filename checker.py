import requests
import os
import time
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
            response = response.json()
            response_status = response["status"]
            if response_status == "found":
                lesson = response["new_attempts"][0]
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
                payloads = {"timestamp": response["timestamp_to_request"]}
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
