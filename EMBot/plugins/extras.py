from EMBot import evil
from telethon import events, Button
from EMBot.status import *
from datetime import timedelta
import os
import requests

@evil.on(events.NewMessage(pattern="[!?/]spem"))
@is_admin
async def spam(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("That's not a user!")
       return
    ree = (await event.get_reply_message()).sender_id
    check = await evil.get_permissions(event.chat_id, ree)

    if check.is_admin:
       await event.reply("He can be a spammer, but he is also an admin!")
       return
    elif check.is_creator:
       await event.delete()
       await event.reply("He is chat creator")
       return
    elif msg.sender.bot:
       await event.delete()
       await event.reply("Its a bot!")
       return

    re = (await event.get_reply_message()).sender_id
    user = await evil.get_entity(ree)
    await event.delete()
    await evil.edit_permissions(event.chat_id, re, timedelta(hours=1), send_messages=False)
    await evil.send_message(event.chat_id, f"[{user.first_name}](tg://user?id={re}) it looks like you are spamming the chat!\nAnd so has been muted for 1 hour")

