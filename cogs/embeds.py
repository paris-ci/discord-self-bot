# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import discord
from discord.ext import commands


class Embeds():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def embed(self, ctx, *, text):
        """Create an embed with the specified text"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed()
        #embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.description = text
        await self.bot.say(embed=embed)






def setup(bot):
    bot.add_cog(Embeds(bot))