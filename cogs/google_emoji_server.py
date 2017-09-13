# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import discord
import time
from discord.ext import commands


class google_emoji_server:
    def __init__(self, bot):
        self.bot = bot
        self.time_last_invite = 0
        self.time_last_join = 0
        self.last_join = None


    async def on_message(self, message):
        if str(message.channel.id) != "313448663655383041":
            return

        self.time_last_invite = time.time()

        await self.bot.send_message(self.bot.get_channel("241994174235279360"), message.content)

    async def on_member_join(self, member):
        if str(member.server.id) != "272885620769161216":
            return
        else:
            self.time_last_join = time.time()
            self.last_join = member
            await self.bot.send_message(self.bot.get_channel("241994174235279360"), "Last invite on Google Emoji Server was used in " + str(self.time_last_join - self.time_last_invite) + " seconds... That's fast")
            await self.bot.send_message(self.bot.get_channel("241994174235279360"), "Last member joining was : " + self.last_join.name + "#" + str(self.last_join.discriminator) + "( <@" + str(self.last_join.id) + "> )")

    @commands.command(pass_context = True)
    async def gjoin(self, ctx):
        await self.bot.delete_message(ctx.message)
        if self.last_join is not None:
            await self.bot.say("Last invite on Google Emoji Server was used in " + str(self.time_last_join - self.time_last_invite) + " seconds... That's fast")
            await self.bot.say("Last member joining was : " + self.last_join.name + "#" + str(self.last_join.discriminator) + "( <@" + str(self.last_join.id) + "> )")
        else:
            await self.bot.say("Wait for someone to join before")


def setup(bot):
    bot.add_cog(google_emoji_server(bot))