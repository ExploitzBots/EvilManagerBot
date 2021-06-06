#    TelethonGPBot
#    Copyright (C) 2021 TgxBots

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/TgxBots/TelethonGPBot/blob/master/LICENSE > 
#    for the license.

from telethon import TelegramClient
import logging
from Configs import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('Stark', api_id=Config.APP_ID, api_hash=Config.API_HASH)
Stark = bot.start(bot_token=Config.TOKEN)
