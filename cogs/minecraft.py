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
from mcstatus import MinecraftServer

logger = logging.getLogger('selfbot')
log_prefix = "[MC] "


def log_debug(message):
    # logger.debug(log_prefix + str(message))
    pass


def log_info(message):
    logger.info(log_prefix + str(message))


class minecraft:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def mcping(self, ctx, host:str, port:int=25565):
        await self.bot.delete_message(ctx.message)
        server = MinecraftServer.lookup(host, port)
        status = server.status()
        await self.bot.say("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

    @commands.command(pass_context=True)
    async def mcplayers(self, ctx, host:str, port:int=25565):
        await self.bot.delete_message(ctx.message)
        server = MinecraftServer.lookup(host, port)
        query = server.query()
        await self.bot.say("The server has the following players online: {0}".format(", ".join(query.players.names)))




def setup(bot):
    bot.add_cog(minecraft(bot))
