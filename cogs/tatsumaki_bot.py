# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import asyncio
import re

import discord
import logging
from discord.ext import commands


logger = logging.getLogger('selfbot')
log_prefix = "[TATSU] "

def log_debug(message):
    # logger.debug(log_prefix + str(message))
    pass


def log_info(message):
    logger.info(log_prefix + str(message))



class tatsumaki_bot:
    def __init__(self, bot):
        self.bot = bot
        self.rep_regex =  re.compile(":up:  \|  (.*) has given .* a reputation point!", re.MULTILINE)
        self.daily_regex =  re.compile(":atm:  \|  (.*) has given .* :yen: (.*) daily credits!", re.MULTILINE)

    async def on_message(self, message):
        if str(message.author.id) == "172002275412279296":
            if self.bot.user in message.mentions:
                pass
                # :up:  |  NAME has given @eyesofcreeper a reputation point!
                m = re.search(self.rep_regex, message.content)
                if m:
                    name = m.group(1)
                    log_info("{n} game me a rep point".format(n=name))
                    await self.bot.send_message(message.channel, "t!rep {n}".format(n=name))
                m = re.search(self.daily_regex, message.content)
                if m:
                    name = m.group(1)
                    credits = m.group(2)
                    log_info("{n} game me {c} credits".format(n=name, c=credits))
                    await self.bot.send_message(message.channel, "t!daily {n}".format(n=name))




    @commands.group()
    async def tatsumaki(self):
        """humm"""
        pass

    @tatsumaki.command(pass_context=True)
    async def fish(self, ctx, times:int):
        for i in range(times):
            await self.bot.send_message(ctx.message.channel, "!fish")
            await asyncio.sleep(30)



def setup(bot):
    bot.add_cog(tatsumaki_bot(bot))