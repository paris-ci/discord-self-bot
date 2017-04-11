# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import discord
from discord.ext import commands

async def send_embed(bot, message, embed, user=None):
    edit_message = ":arrow_up: :arrow_up: :arrow_down: :arrow_down: :arrow_left: :arrow_right: :arrow_left: :arrow_right: :b: :a:"

    if user:
        await bot.edit_message(message, new_content=user.mention, embed=embed)
    else:
        await bot.edit_message(message, new_content=edit_message, embed=embed)

class Faq():
    def __init__(self, bot):
        self.bot = bot
        self.footer = "Selfbot made by Eyesofcreeper"


    @commands.group(pass_context=True)
    async def faq(self, ctx):
        """Get info on multiple topics"""
        #await self.bot.delete_message(ctx.message)
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid faq command passed...')
            await self.bot.say("""```
- * <- You are here
- duckhunt
  |- *
  |- website
  |- howtoplay
  |- howtoconfigure
  |- noselfhost
  |- typebang
- dbots
  |- *
  |- addbot
- selfbot


```""")

    @faq.group(pass_context=True)
    async def duckhunt(self, ctx):

        if str(ctx.invoked_subcommand) == "faq duckhunt":
            embed = discord.Embed()
            embed.colour = discord.Colour.dark_green()
            embed.title = "DuckHunt"
            embed.url = "https://api-d.com"
            embed.description = "DuckHunt is a game I developed. Named as the game on NES, the goal is to be the best duck hunter on a server."
            embed.add_field(name="How does it works ?", value="You have to kill ducks, using the command `!bang`. But there is more than that. You’ll have to reload your weapon (use `!reload`), buy objects to improve efficiency or to piss off other hunters.", inline=False)
            embed.add_field(name="Sound impressive !", value="Yeah, I have to admit that the game is really fun", inline=False)
            embed.add_field(name="I'd like to learn more", value="Our website will help you ! Go to https://api-d.com/", inline=False)
            embed.set_image(url="https://api-d.com/duckhunt.jpg")
            embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
            await send_embed(self.bot, ctx.message, embed)

    @duckhunt.command(name="website", pass_context=True)
    async def dh_website(self, ctx, user:discord.Member = None):
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        embed.title = "DuckHunt - Website"
        embed.url = "https://api-d.com"
        embed.description = "Our website is brand new and online at https://api-d.com."
        embed.add_field(name="Install the bot", value="https://api-d.com/install-the-bot.html", inline=False)
        embed.add_field(name="Bot settings", value="https://api-d.com/bot-settings.html", inline=False)
        embed.add_field(name="Shop items", value="https://api-d.com/shop-items.html", inline=False)
        embed.add_field(name="Command list", value="https://api-d.com/command-list.html", inline=False)
        embed.add_field(name="Need more help ?", value="Join the official duckhunt discord server at https://discordapp.com/invite/2BksEkV", inline=False)
        #embed.set_image(url="https://api-d.com/duckhunt.jpg")
        embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
        await send_embed(self.bot, ctx.message, embed, user)

    @duckhunt.command(name="howtoplay", pass_context=True)
    async def dh_howtoplay(self, ctx, user:discord.Member = None):
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        embed.title = "DuckHunt - How to play"
        embed.url = "https://api-d.com"
        embed.description = "DuckHunt is a simple game to play, but there are many things you can do! Once you see a duck (-,,.-'`'°-,,.-'`'°  _º-  COUAAACK), you can start to play."
        embed.add_field(name="Most used commands", value="Of course, `!bang` and `!reload` are the most important commands. If you see a duck, you'll have to type `!bang` to kill it. But, beware, you weapon can jam, run out of bullets and many things more. If it's the case, try to `!reload` it.", inline=False)
        embed.add_field(name="Shop", value="If you have enough experience points, you can buy some items from this list: https://api-d.com/shop-items.html with you experience using the command `!shop [item number]`. For exemple, you can buy another bullet with `!shop 1` ", inline=False)
        embed.add_field(name="Git gud", value="To be the best hunter, you need to be aware of a lot of statistics. You can see them with `!duckstats` . You should also view the top scores on the channel with `!top`", inline=False)
        embed.add_field(name="Full command list", value="There is a lot more to discorver. You can always view the full command list here : https://api-d.com/command-list.html", inline=False)
        embed.add_field(name="Need more help ?", value="Join the official duckhunt discord server at https://discordapp.com/invite/2BksEkV", inline=False)
        #embed.set_image(url="https://api-d.com/duckhunt.jpg")
        embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
        await send_embed(self.bot, ctx.message, embed, user)

    @duckhunt.command(name="howtoconfigure", pass_context=True, aliases=["howtosetup", "config", "setup"])
    async def dh_howtoconfigure(self, ctx, user:discord.Member = None):
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        embed.title = "DuckHunt - How to configure the bot"
        embed.url = "https://api-d.com"
        embed.description = "Configuring the bot is easy, but you'll have to follow the instructions carefully"
        embed.add_field(name="Invite the bot", value="If you haven't done so already, you will have to invite the bot by clicking here : https://discordapp.com/oauth2/authorize?&client_id=187636051135823872&scope=bot&permissions=68320256", inline=False)
        embed.add_field(name="Claim the server", value="You have invited the bot and given him the required permissions ? Great ! Now it's time to type on **any** channel the `!claimserver` command to make yourself a server admin on the bot. ", inline=False)
        embed.add_field(name="Create channels", value="You will now need to be on the channel(s) where you want ducks to spawn on. Type `!add_channel` on each of them. ", inline=False)
        embed.add_field(name="Warp up", value="The bot is set up with the default configuration. You can change settings with the `!settings set [parameter] [value]`. See the available settings table at http://api-d.com/bot-settings.html", inline=False)
        embed.add_field(name="Need more help ?", value="Join the official duckhunt discord server at https://discordapp.com/invite/2BksEkV", inline=False)
        #embed.set_image(url="https://api-d.com/duckhunt.jpg")
        embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
        await send_embed(self.bot, ctx.message, embed, user)

    @duckhunt.command(name="noselfhost", pass_context=True, aliases=["selfhost"])
    async def dh_noselfhost(self, ctx, user:discord.Member = None):
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        embed.title = "DuckHunt - Please do not self host it"
        embed.url = "https://api-d.com"
        embed.description = "In the past, a lot of users wanted to self host their own copy of duckhunt. Self hosting is possible, but I **strongly** discourage it."
        embed.add_field(name="1st reason", value="Servers Admins want to self host to have a better uptime, or more control, but the official bot already have 99.8% of uptime. A lot of control is provided with the settings command, there isn't anything else to configure. ", inline=False)
        embed.add_field(name="2nd reason", value="Self hosting is bad because I can't see bugs, stats and a lot of metrics I use to guess what I should do first", inline=False)
        embed.add_field(name="3rd reason", value="Self hosting the bot leans you'll get (almost) no support and you will be left alone trying to install it. Updates to the git repo are frequent and you'll have to do them quickly on each release. ", inline=False)
        embed.add_field(name="4rd reason", value="If you self hosted and want to go back to the official version, you can. I can't merge two databases, as this implies a security risk for me and the users.", inline=False)
        embed.add_field(name="Need more help ?", value="A lot of others resons exist. You may discuss that with us on the official duckhunt discord server at https://discordapp.com/invite/2BksEkV", inline=False)
        #embed.set_image(url="https://api-d.com/duckhunt.jpg")
        embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
        await send_embed(self.bot, ctx.message, embed, user)

    @duckhunt.command(name="typebang", pass_context=True)
    async def dh_typebang(self, ctx, user:discord.Member = None):
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        embed.title = "DuckHunt - When you see a duck"
        embed.url = "https://api-d.com"
        embed.description = "Here is a quick hint for ya... Once you see a duck, type `!bang`. Type `!reload` after to reload your weapon or to unstuck it."
        embed.add_field(name="What's a duck ?", value="A duck looks like this : `-,,.-'`'°-,,.-'`'°  _º-  COUAAACK`.", inline=False)
        embed.add_field(name="Full command list", value="There is a lot more commands. View the full command list here : https://api-d.com/command-list.html", inline=False)
        embed.add_field(name="Need more help ?", value="Join the official duckhunt discord server at https://discordapp.com/invite/2BksEkV", inline=False)
        embed.set_image(url="https://api-d.com/duckhunt.jpg")
        embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
        await send_embed(self.bot, ctx.message, embed, user)


    @faq.group(pass_context=True)
    async def dbots(self, ctx):

        if str(ctx.invoked_subcommand) == "faq dbots":
            embed = discord.Embed()
            embed.colour = discord.Colour.dark_green()
            embed.title = "Discord Bots"
            embed.url = "https://bots.discord.pw"
            embed.description = "Discord bots is a server with a lot of bots on it. Guess thre is more than 9000 members and bots on it now."
            embed.add_field(name="How can I join ?", value="Use this invite : https://discord.gg/0cDvIgU2voWn4BaD", inline=False)
            embed.add_field(name="Can I add my bot", value="Yeah, of course, it's the point of this. See the channel #bot-list for more information", inline=False)
            embed.add_field(name="I'd like to learn more", value="Their website is here : https://bots.discord.pw ", inline=False)
            embed.set_image(url="http://api-d.com/snaps/dbots.png")
            embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
            await send_embed(self.bot, ctx.message, embed)


    @dbots.command(name="addbot", pass_context=True)
    async def dbots_addbot(self, ctx, user:discord.Member = None):
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        embed.title = "Discord Bots - How do I add my bot to the server"
        embed.url = "https://bots.discord.pw"
        embed.description = "Adding you bot to the Discord Bots server require knowing the basics of HTML, but it's not very long."
        embed.add_field(name="How do I start ?", value="""
To get your bot added to the list, simply fill out the form on this website https://bots.discord.pw and wait for it to be verified. To increase the chances of that happening:
- Put some effort into the descriptions. "Just another random bot" or similar is not a good description.
- Don't mention/DM a moderator about verifying your bot.
- Make sure both your bot and yourself are online so we can ask you if we have any questions.
- While not a requirement by any means, it also helps if you and your bot have a decent avatar""", inline=False)
        embed.add_field(name="How do I write a description", value="Descriptions are written in HTML", inline=False)
        embed.add_field(name="Need more help ?", value="Join the Discord Bots server at https://discord.gg/0cDvIgU2voWn4BaD", inline=False)
        embed.set_image(url="http://api-d.com/snaps/dbots.png")
        embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
        await send_embed(self.bot, ctx.message, embed, user)



    @faq.command(pass_context=True)
    async def selfbot(self, ctx, user:discord.Member = None):
        embed = discord.Embed()
        embed.colour = discord.Colour.dark_green()
        embed.title = "Selfbot"
        #embed.url = "https://api-d.com"
        embed.description = "A selfbot is a bot connected to your user account. It's what I'm using for the faq. I am the only one who can control it."
        embed.add_field(name="Is it permitted ?", value="Of course, as long as it's a user that you really use. To create a real bot, see https://discordapp.com/developers/docs/intro", inline=False)
        embed.add_field(name="Why should I use one ?", value="I don't know. Most of things can be done with normal bots. User bots are useful if you need some command to be available everywhere & just for you. If you don't know, don't use one...", inline=False)
        embed.add_field(name="Need more help ?", value="Join the discord bots server at https://discord.gg/0cDvIgU2voWn4BaD and the discord api server at https://discord.gg/discord-api", inline=False)
        embed.set_image(url="https://discordapp.com/assets/c7d26cb2902f21277d32ad03e7a21139.gif")
        embed.set_footer(text=self.footer, icon_url=self.bot.user.avatar_url)
        await send_embed(self.bot, ctx.message, embed, user)







def setup(bot):
    bot.add_cog(Faq(bot))