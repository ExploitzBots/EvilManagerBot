
from telethon import TelegramClient
import logging
from Configs import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('Evil', api_id=Config.APP_ID, api_hash=Config.API_HASH)
Evil = bot.start(bot_token=Config.TOKEN)
