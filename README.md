# review_check_bot

The script is designed to notify [devman.org](https://dvmn.org/) students about the status of 
their tasks that are being reviewed. 

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Before use, you need to set DVMN_TOKEN, TG_TOKEN, TG_CHAT_ID in `.env` file.
```
DVMN_TOKEN=
TG_TOKEN=
TG_CHAT_ID=
LOGGER_BOT_TOKEN=
ADMIN_CHAT_ID=
```
To receive notification in telegram run `tg_bot.py`:
```
python tg_bot.py
```
### Running in a container

First, build the container image using the following command:
```
docker build -t review_bot .  
```
After the image has been built, you can start a container by running the following command:
```
docker run -d --env-file .env review_bot 
```
This will start the container in detached mode with environment variables set in the .env file.