import logging
from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils

# Setting up logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Logging that bot is starting
logging.info("Bot is starting...")

# Adjust chat and channel ID limits
pyrogram.utils.MIN_CHAT_ID = -1002092954715
pyrogram.utils.MIN_CHANNEL_ID = -1002092954715

# Initialize the bot client
bot = Client("ghost", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

# Log whether a string session is provided
if STRING_SESSION:
    logging.info("String session provided. Starting multiple clients (bot and Client2)...")
    apps = [Client2, bot]
    for app in apps:
        app.start()
        logging.info(f"{app} started successfully.")

    # Keep the bot running
    logging.info("Bot is now idle, waiting for events...")
    idle()

    # Stopping clients after idle
    for app in apps:
        app.stop()
        logging.info(f"{app} stopped successfully.")
else:
    logging.info("No string session provided. Starting only the bot.")
    bot.run()
    logging.info("Bot is running.")