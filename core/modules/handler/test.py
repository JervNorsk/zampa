from config import Config
import requests
import datetime 
import json

api_key= Config.BOT_TOKEN

def telegram_api(update,context):
    bot = context.bot
    url = "https://api.telegram.org/bot{}/getUpdates".format(api_key)
    response = requests.get(url)
    data=response.json()
    bot.send_message(update.message.chat_id,data)