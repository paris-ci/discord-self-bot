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


class maths_bot:
    def __init__(self, bot):

        self.cure = False
        self.activated = False  # Auto Activate the bot. You'll have to activate it with >maths activate otherwise

        self.bot = bot

        # Charged! +57
        # Power: 57 / 200
        self.dropped_regex = re.compile(".* `(.*)` .*", re.MULTILINE)


    async def on_message(self, message):
        """doc"""
        if not str(message.author.id) == "228984079985541120":
            return



        matched = False
        to_dispatch = []

        content = str(message.content)
        log_debug("Processing maths message :\n" + content)

        m = re.search(self.dropped_regex, content)
        if m:
            matched = True
            log_debug("Matched dropped regex")
            equation = m.group(1).replace("x", "*")
            log_info("Got equation : {eq}".format(eq=equation))

            result = round(parser.parse(equation).evaluate({}), 2)
            log_info("Result is : {res}".format(res=result))
            to_dispatch.append(".take {res}".format(res=result))

        if self.activated:
            for action in to_dispatch:
                await self.bot.send_message(message.channel, action)

        if not matched:
            log_info("Message not matched ! : \n" + content)

    @commands.group()
    async def maths(self):
        pass

    @maths.command(aliases=["stop", "start", "toggle"], pass_context=True)
    async def activate(self, ctx):
        if not self.activated:
            self.activated = True
            await self.bot.edit_message(ctx.message, ":ok: Sucessfully activated :D")
        else:
            self.activated = False
            await self.bot.edit_message(ctx.message, ":ok: Sucessfully stopped :D")



def setup(bot):
    bot.add_cog(maths_bot(bot))
