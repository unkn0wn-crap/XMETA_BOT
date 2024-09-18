from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client , filters
from script import *
from config import *





@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
    text = script.ABOUT_TXT.format(bot.me.mention)
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "home")]
                  ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("Admin",url = "https://t.me/corpsealone"),
        InlineKeyboardButton("Close",callback_data = "cancel") ]])
    await message.reply_text(text = text,reply_markup = keybord)    



@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["admin"]))
async def admincm(bot,message):
    text = script.ADMIN_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("✖️ Close ✖️",callback_data = "cancel") ]])
    await message.reply_text(text = text,reply_markup = keybord)    



@Client.on_callback_query(filters.regex('help'))
async def help(bot,update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keybord = InlineKeyboardMarkup([ 
                    [InlineKeyboardButton('Tʜᴜᴍʙɴᴀɪʟ', callback_data='thumbnail'),
                    InlineKeyboardButton('Cᴀᴘᴛɪᴏɴ', callback_data='caption')],
                    [InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
                    [InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ',callback_data='metadata'),
                    InlineKeyboardButton('Dᴏɴᴀᴛᴇ', callback_data='donate')]
                   ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_callback_query(filters.regex('thumbnail'))
async def thumbnail(bot,update):
    text = script.THUMBNAIL_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('caption'))
async def caption(bot,update):
    text = script.CAPTION_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('donate'))
async def donate(bot,update):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('metadata'))
async def metadata(bot,update):
    text = script.METADATA_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_callback_query(filters.regex('home'))
async def home_callback_handler(bot, query):
    text = f"""Oᴋ Sᴏ ᴛʜɪs ɪs ᴍᴇᴛᴀᴅᴀᴛᴀ + ғɪʟᴇ ʀᴇɴᴀᴍɪɴɢ ʙᴏᴛ
  {message.from_user.mention} \n\n \n\nUsɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇs\n\nYᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ\n\nBᴏᴛ Aʟsᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("Dev", url="https://t.me/ghost_kun")],
        [InlineKeyboardButton("Support", url="https://t.me/yukilogs")],
        [InlineKeyboardButton("Help", callback_data='help'),
        InlineKeyboardButton("Blyat", callback_data='about')]
        ])
    await query.message.edit_text(text=text, reply_markup=keybord)







# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper & @MadflixOfficials
