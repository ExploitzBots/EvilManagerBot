from EMBot import Evil
from telethon import events, Button

PM_START_TEXT = """
**Hɪ {}**
Mʏ Sᴇʟғ Gʀᴏᴜᴘ Mᴀɴᴀɢᴇʀ Bʙᴛ Wɪᴛʜ Mᴀʙʏ Oᴛʜᴇʀ Mɪᴅᴜᴋᴇs Tʜᴀᴛ Wɪʟʟ Mᴀᴋᴇ Yᴏᴜʀ TG Lɪғᴇ Eᴀsʏ As Fᴜ*ᴋ. 

**Cʟɪᴄᴋ Tʜᴇ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Tᴏ Sᴇᴇ Wʜᴀʀ I Cᴀɴ Fᴏ**
"""

@Evil.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help And Command 👨‍🔧", data="help")],
        [Button.inline("Donate ❤️ ", data= "donate")]])
       return

    if event.is_group:
       await event.reply("**I am alive sir!**")
       return
