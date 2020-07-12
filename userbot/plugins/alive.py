"""Check if userbot alive or not . """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PUT VALUE IN ALIVE_NAME"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**I AM  RUNNING SUCCESFULLY**\n\n"
                     f"`Telethon version📱: {version.__version__}\n\n`"
                     f"`Python Version🐍: {python_version()}\n\n`"
                     "`Bot was modified by✨:` Pro(s)\n\n"
                     "`Database Status🐱‍👤: Databases functioning normally!\n\n`"
                     "`Always with you, my master!\n\n`"
                     f"`MY OWNER😎`:   {DEFAULTUSER}\n\n\n")
                 

CMD_HELP.update({
    "alive":
    ".alive\
    \nUsage: Type .alive to see wether your bot is working or not.\
    "
})    
