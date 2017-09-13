# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import asyncio
import logging
import re

from discord.ext import commands

logger = logging.getLogger('selfbot')
log_prefix = "[WINTER] "


def log_debug(message):
    # logger.debug(log_prefix + str(message))
    pass


def log_info(message):
    logger.info(log_prefix + str(message))


class winter_bot:
    def __init__(self, bot):

        self.cure = False
        self.activated = False  # Auto Activate the bot on gcharge. You'll have to activate it with >winter activate otherwise

        self.current_HP = 0
        self.max_HP = 0
        self.current_charge = 0
        self.max_charge = 0
        self.multiplicator = 0
        self.enemy_hp = 0

        self.bot = bot

        # Charged! +57
        # Power: 57 / 200
        self.charge_regex = re.compile("^Power: (\d*) / (\d*)", re.MULTILINE)

        # ```ini
        # [Enemy][HP: 78%][Cr X2]
        # Damage dealt: MISS
        # Weakness: Electric claws I
        #
        # «PLAYER: Eyesofcreeper»
        # HP: <•••-------> 19% (391 / 2100)
        # Damage received: 1293
        # ```
        self.attack_regex = re.compile("```ini\n"
                                       "\[Enemy]\[HP: (?P<enemy_pct_life>\d*)%]\[Cr X(?P<credits_multiplicator>\d*)]\n"
                                       "Damage dealt: (?P<damage_dealt>.*)\n"
                                       "(?:CRITICAL!!\n)?"
                                       "(?:Weakness: .*\n)?"
                                       "\n"
                                       "«PLAYER: (?P<player_name>.*)»\n"
                                       "HP: .* (?P<pct_HP>\d*)% \((?P<current_HP>\d*) / (?P<max_HP>\d*)\)\n"
                                       "Damage received: (?P<damage_taken>.*)\n"
                                       "```", re.MULTILINE)

        # **You lose**
        # TURNS: 3
        self.lost_regex = re.compile("\*\*You lose\*\*\n"
                                     "TURNS: (\d*)")

        # @Eyesofcreeper, You won!
        # Turns: 1
        # Credits: 6
        # Experience: 14
        self.won_regex = re.compile("You won!\n"
                                    "Turns: (\d*)\n"
                                    "Credits: (\d*)\n"
                                    "Experience: (\d*)")

    async def on_message(self, message):
        """doc"""
        if not str(message.author.id) == "241768807276740608":
            return



        matched = False
        to_dispatch = []

        content = str(message.content)
        log_debug("Processing winter message :\n" + content)

        m = re.search(self.charge_regex, content)
        if m:
            matched = True
            log_debug("Matched charge regex")
            current_power = int(m.group(1))
            max_power = int(m.group(2))

            log_info("Charged at {pct}% ({current}/{max})".format(pct=int(current_power / max_power * 100),
                                                                  current=current_power,
                                                                  max=max_power))

            self.current_charge = int(current_power)
            self.max_charge = int(max_power)

            if current_power == max_power:
                to_dispatch.append("gattack")
            else:
                to_dispatch.append("gcharge")

        m = re.search(self.attack_regex, content)

        if m:
            matched = True

            attack_results = m.groupdict()
            if attack_results["player_name"] == self.bot.user.display_name:

                log_info("Attack damage {damage_dealt}. We took {damage_taken} damage. Enemy HP is at {enemy_pct}%. Own HP is at {hp_pct}% ({current}/{max}). Credits multiplicator is at {multiplicator}".format(
                        damage_dealt=attack_results["damage_dealt"] if not "MISS" else 0,
                        enemy_pct=attack_results["enemy_pct_life"],
                        hp_pct=int(int(attack_results["current_HP"]) / int(attack_results["max_HP"]) * 100),
                        current=attack_results["current_HP"],
                        max=attack_results["max_HP"],
                        damage_taken=attack_results["damage_taken"] if not "MISS" else 0,
                        multiplicator=attack_results["credits_multiplicator"]))

                self.current_HP = int(attack_results["current_HP"])
                self.max_HP = int(attack_results["max_HP"])
                self.current_charge = 0
                self.multiplicator = int(attack_results["credits_multiplicator"])
                self.enemy_hp = int(attack_results["enemy_pct_life"])

                if not int(attack_results["current_HP"]) >= int(int(attack_results["max_HP"]) / 2) and self.cure:
                    log_info("Curing for low HP")
                    to_dispatch.append("gcure")

                to_dispatch.append("gcharge")
            else:
                log_debug("Not us :'(")

        m = re.search(self.lost_regex, content)

        if m:
            matched = True
            log_debug("Matched lost regex")
            if self.bot.user in message.mentions:
                turns = int(m.group(1))
                log_info("Lost in {turns} turns :(".format(turns=turns))

                self.multiplicator = 0
                self.enemy_hp = 100
                to_dispatch.append("gcharge")
            else:
                log_debug("Not us")

        m = re.search(self.won_regex, content)

        if m:
            matched = True
            log_debug("Matched won regex")
            if self.bot.user in message.mentions:
                turns = int(m.group(1))
                credits = int(m.group(2))
                experience = int(m.group(3))
                log_info("Won in {turns} turns. Earned {credits} credits and {exp} experience points".format(turns=turns,
                                                                                                             credits=credits,
                                                                                                             exp=experience))

                self.current_charge = 0
                self.multiplicator = 0
                self.enemy_hp = 100

                to_dispatch.append("gcharge")

            else:
                log_debug("Not us")

        if self.activated:
            for action in to_dispatch:
                await asyncio.sleep(6)  # Cooldown
                await self.bot.send_message(message.channel, action)

        if not matched:
            log_info("Message not matched ! : \n" + content)

    @commands.group()
    async def winter(self):
        pass

    @winter.command(aliases=["stop", "start", "toggle"], pass_context=True)
    async def activate(self, ctx):
        if not self.activated:
            self.activated = True
            await self.bot.edit_message(ctx.message, ":ok: Sucessfully activated :D")
        else:
            self.activated = False
            await self.bot.edit_message(ctx.message, ":ok: Sucessfully stopped :D")

    @winter.command(aliases=["info", "stats", "scores", "status"], pass_context=True)
    async def current(self, ctx):

        def generate_bar(current: int = 0, max_value: int = 0, emoji_on: str = ":black_small_square:", emoji_off: str = ":white_small_square:", size: int = 10):
            size_on = int((current / max_value) * size) if max_value != 0 else 0
            topr = emoji_on * size_on
            topr += emoji_off * (size - size_on)
            topr += " {pct}% ({current} / {max})".format(pct=int(current / max_value * 100) if max_value != 0 else 0, current=current, max=max_value)
            return topr

        topr = "Current health : " + generate_bar(current=int(self.current_HP), max_value=int(self.max_HP)) + "\n"
        topr += "Current charge : " + generate_bar(current=int(self.current_charge), max_value=int(self.max_charge)) + "\n"
        topr += "Current multiplicator : " + str(self.multiplicator) + " | Current enemy life " + str(self.enemy_hp) + "%"

        await self.bot.edit_message(ctx.message, topr)


def setup(bot):
    bot.add_cog(winter_bot(bot))
