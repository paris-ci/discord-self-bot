# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import datetime
import json
import random

import discord
import os
from discord.ext import commands

messages = ["He said that lol", "That's not even funny", "lol", "okay", "NO!", "See this ?", "Do you see what I see ?"]

async def get_quote_embed(bot, quote):
    user = discord.utils.find(lambda m: str(m.id) == str(quote["author_id"]), bot.get_all_members() )

    ts = datetime.datetime.fromtimestamp(
            int(quote["timestamp"])
    )
    embed = discord.Embed()
    embed.colour = discord.Colour.orange()
    embed.title = "Quote #" + quote["quote_id"]

    # embed.url = "https://api-d.com"
    embed.description = quote["content"]
    embed.add_field(name="Channel", value=quote["channel"]) if quote["channel"] else ""
    embed.add_field(name="Server", value=quote["server"]) if quote["server"] else "None"
    embed.timestamp= ts

    embed.set_author(name=user.name, icon_url=user.avatar_url)


    # embed.set_image(url="")
    embed.set_footer(text="Said by " + quote["author_name"] + "#" + quote["author_discriminator"])
    return embed


class Quotes:
    def __init__(self, bot):
        self.bot = bot
        self.dir = self.bot.where + "quotes" + os.sep

    @commands.group(aliases=["q", "quote"])
    async def quotes(self):
        pass

    @quotes.command(pass_context=True, name="new", aliases=["add"])
    async def qnew(self, ctx, mid:int):

        message = discord.utils.find(lambda m: str(m.id) == str(mid), self.bot.messages)

        if message is None :
            await self.bot.say("Can't find this message :( It may be too old")
            return


        with open(self.dir + "current.txt", "r") as infile:
            n = infile.read()
            file = self.dir + "quote_" + str(n).rjust(5, '0') + ".json"

        saving = {
            "message_id"          : message.id,
            "content"             : message.content,
            "clean_content"       : message.clean_content,
            "channel"             : message.channel.name,
            "server"              : message.server.name if message.server else None,
            "author_name"         : message.author.name,
            "author_id"           : message.author.id,
            "author_mention"      : message.author.mention,
            "author_discriminator": message.author.discriminator,
            "timestamp"           : message.timestamp.timestamp(),
            "attachments"         : message.attachments,
            "quote_id"            : n
        }

        with open(file, 'w') as outfile:
            json.dump(saving, outfile, sort_keys=True, indent=4, separators=(',', ': '))

        with open(self.dir + "current.txt", "w") as outfile:
            outfile.write(str(int(n) + 1))

        await self.bot.edit_message(ctx.message, new_content=random.choice(messages), embed=await get_quote_embed(self.bot, saving))

    @quotes.command(pass_context=True, name="view")
    async def qview(self, ctx, qid:int):
        try:
            with open(self.dir + "quote_" + str(qid).rjust(5, '0') + ".json", "r") as infile:
                q = json.loads(infile.read())
        except IOError:
            await self.bot.say("Unknown quote")
            return
        await self.bot.edit_message(ctx.message, new_content=random.choice(messages), embed=await get_quote_embed(self.bot, q))


def setup(bot):
    bot.add_cog(Quotes(bot))
