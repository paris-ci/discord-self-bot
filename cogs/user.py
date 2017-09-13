# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""

import discord
from discord.ext import commands


def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True

    return check

class Userinfo:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hierarchy(self, ctx, member:discord.Member):
        await self.bot.delete_message(ctx.message)
        topr = "**Hierarchy for {member}**\n\n".format(member=member.mention)
        for role in sorted(member.server.roles, key=lambda r: r.position, reverse=True):
            if role in member.roles:
                topr += "- **" + role.name.replace("@", "") + "**\n"
            else:
                topr += "- " + role.name.replace("@", "") + "\n"

        await self.bot.say(topr)


    @commands.command(pass_context=True)
    async def permissions(self, ctx, member:discord.Member):
        await self.bot.delete_message(ctx.message)
        channel = ctx.message.channel
        permissions = channel.permissions_for(member)

        have_perms = ""
        dosnt_have_perms = ""

        position = str(member.top_role.position) + "/" + str(len(member.server.roles))

        roles = ""

        for role in member.roles:
            roles += "- " + role.name.replace("@", "") + "\n"

        for permission, value in permissions:
            if value:
                have_perms += "- " + permission + "\n"
            else:
                dosnt_have_perms +=  "- " + permission + "\n"

        await self.bot.say("""**Permissions for {member} on {channel}:**
Roles:
{roles}
Top role is at position: {pos}
Permissions granted: 
{have}
Permissions not granted: 
{dont_have}
""".format(member=member.mention, channel="#" + channel.name, have=have_perms, dont_have=dosnt_have_perms, roles=roles, pos=position))



    @commands.command(pass_context=True)
    async def info(self, ctx):
        """Get user info. Ex: >info @user"""
        if ctx.invoked_subcommand is None:
            name = ctx.message.content[5:].strip()
            if name:
                try:
                    name = ctx.message.mentions[0]
                except:
                    name = ctx.message.server.get_member_named(name)
                if not name:
                    await self.bot.send_message(ctx.message.channel, self.bot.bot_prefix + 'Could not find user.')
                    return
            else:
                name = ctx.message.author

            # Thanks to IgneelDxD for help on this
            if name.avatar_url[60:].startswith('a_'):
                avi = 'https://images.discordapp.net/avatars/' + name.avatar_url[33:][:18] + name.avatar_url[59:-3] + 'gif'
            else:
                avi = name.avatar_url

            if embed_perms(ctx.message):
                em = discord.Embed(timestamp=ctx.message.timestamp, colour=0x708DD0)
                em.add_field(name='User ID', value=name.id, inline=True)
                em.add_field(name='Nick', value=name.nick, inline=True)
                em.add_field(name='Status', value=name.status, inline=True)
                em.add_field(name='In Voice', value=name.voice_channel, inline=True)
                em.add_field(name='Account Created', value=name.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.add_field(name='Join Date', value=name.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_thumbnail(url=avi)
                em.set_author(name=name, icon_url='https://i.imgur.com/RHagTDg.png')
                await self.bot.send_message(ctx.message.channel, embed=em)
            else:
                msg = '**User Info:** ```User ID: %s\nNick: %s\nStatus: %s\nIn Voice: %s\nAccount Created: %s\nJoin Date: %s\nAvatar url:%s```' % (name.id, name.nick, name.status, name.voice_channel, name.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), name.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), avi)
                await self.bot.send_message(ctx.message.channel, self.bot.bot_prefix + msg)

            await self.bot.delete_message(ctx.message)



def setup(bot):
    bot.add_cog(Userinfo(bot))