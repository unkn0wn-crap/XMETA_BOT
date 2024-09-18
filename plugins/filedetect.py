from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import ForceReply


@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text 
        await message.delete() 
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)

        # Add file extension if not provided
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"  # Default extension
            new_name = new_name + "." + extn
        await reply_message.delete()

        # Automatically process the file as a document
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            # Automatically selecting document
            await process_document(client, file, new_name)
        elif file.media == MessageMediaType.AUDIO:
            await process_audio(client, file, new_name)

async def process_document(client, file, new_name):
    # Code to handle document upload
    await client.send_document(
        chat_id=file.chat.id,
        document=file.file_id,
        file_name=new_name
    )
    # You can add other processing logic here as needed

async def process_audio(client, file, new_name):
    # Code to handle audio upload if needed
    await client.send_audio(
        chat_id=file.chat.id,
        audio=file.file_id,
        file_name=new_name
    )