from pyrogram.errors import FloodWait
import asyncio
from pyrogram import Client, filters
from helper.database import getid, delete
import time
from config import *




@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        ms = await message.reply_text("Gᴇᴛᴛɪɴɢ Aʟʟ IDs Fʀᴏᴍ Dᴀᴛᴀʙᴀsᴇ. Pʟᴇᴀsᴇ Wᴀɪᴛ...")
        ids = getid()
        tot = len(ids)
        success = 0
        failed = 0
        await ms.edit(f"Sᴛᴀʀᴛɪɴɢ Bʀᴏᴀᴅᴄᴀsᴛ... \n\nSᴇɴᴅɪɴɢ Mᴇssᴀɢᴇ Tᴏ {tot} Usᴇʀs")
        for id in ids:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(id)
                success += 1
            except:
                failed += 1
                delete({"_id": id})
                pass
            try:
                await ms.edit(f"Mᴇssᴀɢᴇ Sᴇɴᴛ Tᴏ {success} Cʜᴀᴛs \n\n{failed} Cʜᴀᴛs Fᴀɪʟᴇᴅ Oɴ Rᴇᴄᴇɪᴠɪɴɢ Mᴇssᴀɢᴇ \n\nTᴏᴛᴀʟ - {tot}")
            except FloodWait as e:
                await asyncio.sleep(t.x)