from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils

pyrogram.utils.MIN_CHAT_ID = -1002092954715
pyrogram.utils.MIN_CHANNEL_ID = -1002092954715



bot = Client("ghost", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))



try:
    if STRING_SESSION:
        apps = [Client2, bot]
        for app in apps:
            app.start()
        idle()
        for app in apps:
            app.stop()
    else:
        bot.run()
except Exception as e:
    print(f"An error occurred: {e}")
