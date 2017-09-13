# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import asyncio
import discord
import logging
from discord.ext import commands
logger = logging.getLogger('selfbot')



class text():
    def __init__(self, bot):
        self.bot = bot
        self.start, self.stop = "{", "}"
        self.replacements = \
            {
                "dh_invite": "https://discord.gg/2BksEkV",
                "wat": "https://www.destroyallsoftware.com/talks/wat",
                "bacon_spam": "https://goo.gl/hnByCx\nhttps://goo.gl/rLZ3fz\nhttps://goo.gl/ZQ88oh\nhttps://goo.gl/RJWJa7\nhttps://goo.gl/ezSyhy \nhttps://goo.gl/shWTR3\nhttps://goo.gl/uQKJq7\nhttps://goo.gl/6o0bUK\nhttps://goo.gl/9E8Lqy\nhttps://goo.gl/66yKAq\nhttps://goo.gl/NBQV1T\nhttps://goo.gl/gXCr1m\nhttps://goo.gl/TZQ6Ai\nhttps://goo.gl/R521YA\nhttps://goo.gl/noAavZ\nhttps://goo.gl/ZkhwNg\nhttps://goo.gl/H5mfVf\nhttps://goo.gl/TnP2FY\nhttps://goo.gl/0RHTcZ\nhttps://goo.gl/WGrBN8\nhttps://goo.gl/4nQxt3\nhttps://goo.gl/LXkd0P\nhttps://goo.gl/M5E6fp\nhttps://goo.gl/58bNEQ\nhttps://goo.gl/n0rey7\nhttps://goo.gl/zjS2Q8\nhttps://goo.gl/Dze7Ri\nhttps://goo.gl/cCYZXi\nhttps://goo.gl/twYu9t\nhttps://goo.gl/QXmN7s\nhttps://goo.gl/AB7mao\nhttps://goo.gl/1TK7Ow\nhttps://goo.gl/YC4Yqa\nhttps://goo.gl/lnw70h\nhttps://goo.gl/1eYiMS\nhttps://goo.gl/wr3Blt\nhttps://goo.gl/6AHngn\nhttps://goo.gl/yucTlG\nhttps://goo.gl/Wlwkox\nhttps://goo.gl/HC1zbj\nhttps://goo.gl/gQjsRl\nhttps://goo.gl/xvlK1f",
                "dh_github" : "https://github.com/DuckHunt-discord/DHV2",
                "typing": "••• Several People are typing",
                "cloudflare": "Bad Gateway Connection Error: 506... Failed to connect to server...\nYou/Browser :white_check_mark: > DDoS Protection/CloudFlare :white_check_mark: > Server/domain :x:",
                "pub" : "Vené sure mon server mine crafte sur l'ipé 127.0.0.1, ile faus pa hamachier /s",
                "pls_fix_ban": "Please fix your !ban command (should match `!ban *` not `!ban*`)"
            }

    @commands.command(pass_context=True)
    async def delete_after(self, ctx, seconds:float, *, text:str):
        """doc"""
        await self.bot.delete_message(ctx.message)
        m = await self.bot.send_message(ctx.message.channel, text)
        await asyncio.sleep(seconds)
        await self.bot.delete_message(m)

    @commands.command(pass_context=True)
    async def multiple_messages(self, ctx, *, text:str):
        """doc"""
        await self.bot.delete_message(ctx.message)
        for message in text.split("|"):
            await self.bot.send_message(ctx.message.channel, message)
            await asyncio.sleep(.1)

    @commands.command(pass_context=True)
    async def multiple_messages_delete(self, ctx, *, text:str):
        """doc"""
        l = []
        await self.bot.delete_message(ctx.message)
        for message in text.split("|"):
            l.append(await self.bot.send_message(ctx.message.channel, message))
            await asyncio.sleep(.1)

        for m in l:
            await self.bot.delete_message(m)



    async def on_message(self, message):
        """Replace placeholders in a message by their definition"""
        if not message.author == self.bot.user:
            return
        content = str(message.content)

        ncontent = content.format(**self.replacements)

        if not content == ncontent:
            await self.bot.edit_message(message, new_content=ncontent)



def setup(bot):
    bot.add_cog(text(bot))