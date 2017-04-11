# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.6

"""
Self bot of Eyesofcreeper
"""
import os

from discord.ext import commands
import discord
import datetime, re
import json, asyncio
import copy
import logging
import traceback
import sys
from collections import Counter


try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

initial_extensions = []
for extension in os.listdir("cogs"):
    if extension.endswith('.py'):
        try:
            initial_extensions.append("cogs." + extension.rstrip(".py"))
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))


discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.CRITICAL)
logger = logging.getLogger('selfbot')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
steam_handler.setFormatter(formatter)
logger.addHandler(steam_handler)


help_attrs = dict(hidden=True)

prefix = ['>', '\N{HEAVY EXCLAMATION MARK SYMBOL}']
bot = commands.Bot(command_prefix=prefix, description=__doc__, pm_help=None, help_attrs=help_attrs, self_bot=True)



@bot.event
async def on_ready():
    logger.info('Logged in as:')
    logger.info('Username: ' + bot.user.name)
    logger.info('ID: ' + bot.user.id)
    if not hasattr(bot, 'uptime'):
        bot.uptime = datetime.datetime.utcnow()

@bot.event
async def on_resumed():
    pass

@bot.event
async def on_message(message):
    if not message.author == bot.user:
        #log.info(message.content)

        return

    if message.content.startswith('>'):
        logger.info(message.content)

    await bot.process_commands(message)

def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

if __name__ == '__main__':
    credentials = load_credentials()
    debug = any('debug' in arg.lower() for arg in sys.argv)

    bot.client_id = credentials['client_id']
    bot.prefix = ":robot:"
    bot.where = os.path.dirname(os.path.realpath(__file__)) + os.sep


    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            logger.debug("Loaded : " + str(extension))
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    bot.run(bot.client_id, bot=False)
    handlers = logger.handlers[:]
    for hdlr in handlers:
        hdlr.close()
        logger.removeHandler(hdlr)