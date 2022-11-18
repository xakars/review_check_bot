import telegram
import os
from checker import check_task_status
from dotenv import load_dotenv


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

