# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import asyncio
import logging
import re
import py_expression_eval

parser = py_expression_eval.Parser()
from discord.ext import commands

logger = logging.getLogger('selfbot')
log_prefix = "[MATHS] "


def log_debug(message):
    # logger.debug(log_prefix + str(message))
    pass


def log_info(message):
    logger.info(log_prefix + str(message))


class tests:
    def __init__(self, bot):


        self.bot = bot


    #async def on_message(self, message):
    #    """doc"""
    #    if str(message.channel.id) == "315257219367043082" and not str(message.author.id) == "138751484517941259":
    #        await self.bot.send_message(message.channel, str(int(message.content)+1))



def setup(bot):
    bot.add_cog(tests(bot))
