from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from config import *
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre





@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
    if len(m.command) >= 3:
        try:
            user_id = m.text.split(' ', 2)[1]
            reason = m.text.split(' ', 2)[2]
            await m.reply_text("Nᴏᴛғɪᴇᴅ ᴛʜᴇ ᴜsᴇʀ Sᴜᴄᴇssғᴜʟʟʏ")
            await c.send_message(chat_id=int(user_id), text=reason)
        except:
            await m.reply_text("Usᴇʀ Nᴏᴛ Nᴏᴛғɪᴇᴅ Sᴜᴄᴇssғᴜʟʟʏ")
            
            

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton(" Bᴀsɪᴄ", callback_data="vip1"),
        InlineKeyboardButton("⚡ Sᴛᴀɴᴅᴀʀᴅ", callback_data="vip2")],
        [InlineKeyboardButton("💎 Pʀᴏ", callback_data="vip3")],
        [InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ ✖️",callback_data = "cancel")]
        ])
        
    await message.reply_text("Sᴇʟᴇᴄᴛ Pʟᴀɴ Tᴏ Uᴘɢʀᴀᴅᴇ...", quote=True, reply_markup=button)
    
    

@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("Limit 1GB", callback_data="cp1"),
        InlineKeyboardButton("All Power Cease", callback_data="cp2")],
        [InlineKeyboardButton("✖️ Cancel ✖️",callback_data = "cancel")]
        ])
	
    await message.reply_text("Pᴏᴡᴇʀ Cᴇᴀsᴇ Mᴏᴅᴇ...", quote=True, reply_markup=button)



@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("Yes",callback_data = "dft"),
        InlineKeyboardButton("No",callback_data = "cancel")]
        ])
        
    await message.reply_text(text=f"Do You Really Want To Reset Daily Limit To Default Data Limit 2GB ?", quote=True, reply_markup=button)
    
    
    

# PREMIUM POWER MODE
@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit  = 21474836500
    uploadlimit(int(user_id),21474836500)
    usertype(int(user_id),"Bᴀsɪᴄ")
    addpre(int(user_id))
    await update.message.edit("Aᴅᴅᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ Tᴏ Pʀᴇᴍɪᴜᴍ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 20 GB")
    await bot.send_message(user_id, f"Hey {update.from_user.mention} \n\nYou Are Upgraded To <b>🪙 Basic</b>. Check Your Plan Here /myplan")



@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 53687091200
    uploadlimit(int(user_id), 53687091200)
    usertype(int(user_id),"⚡ Standard")
    addpre(int(user_id))
    await update.message.edit("Added Successfully To Premium Upload Limit 50 GB")
    await bot.send_message(user_id, f"Hey {update.from_user.mention} \n\nYou Are Upgraded To <b>⚡ Standard</b>. Check Your Plan Here /myplan")



@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 107374182400
    uploadlimit(int(user_id), 107374182400)
    usertype(int(user_id),"💎 Pro")
    addpre(int(user_id))
    await update.message.edit("Added Successfully To Premium Upload Limit 100 GB")
    await bot.send_message(user_id, f"Hey {update.from_user.mention} \n\nYou Are Upgraded To <b>💎 Pro</b>. Check Your Plan Here /myplan")





# CEASE POWER MODE 
@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot,update):
    id = update.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit  = 2147483652
    uploadlimit(int(user_id), 2147483652)
    usertype(int(user_id),"⚠️ Account Downgraded")
    addpre(int(user_id))
    await update.message.edit("Added Successfully To Upload Limit 2GB")
    await bot.send_message(user_id, f"Hey {update.from_user.mention} \n\nYou Are Downgraded To Cease <b>Limit 2GB</b>")



@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot,update):
    id = update.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit  = 0
    uploadlimit(int(user_id), 0)
    usertype(int(user_id),"⚠️ Account Downgraded")
    addpre(int(user_id))
    await update.message.edit("Added Successfully To Upload Limit 0GB")
    await bot.send_message(user_id, f"Hey {update.from_user.mention} \n\nYou Are Downgraded To Cease <b>Limit 0GB</b>. Check Your Plan Here /myplan \n")




# RESET POWER MODE
@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
    id = update.message.reply_to_message.text.split("/resetpower")
    user_id = id[1].replace(" ", "")
    inlimit = 2147483652
    uploadlimit(int(user_id), 2147483652)
    usertype(int(user_id),"🆓 Free")
    addpre(int(user_id))
    await update.message.edit("Daily Data Limit Has Been Reset Successfully.\n\nThis Account Has Default 2GB Remaining Capacity")
    addpre(int(user_id))
    await update.message.edit("Added Successfully To Upload Limit 0GB")
    await bot.send_message(user_id, f"Hey {update.from_user.mention} \n\nYou Are Downgraded To Cease <b>Limit 0GB</b>. Check Your Plan Here /myplan \n")
    await bot.send_message(user_id, f"Hey {update.from_user.mention} \n\nYour Daily Data Limit Has Been Reset Successfully. Check Your Plan Here /myplan\n")