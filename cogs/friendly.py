"""Friendly stuff"""

import discord
from discord.ext import commands
import random

import config as cfg

class Friendly_commands(commands.Cog, name='Friendly Stuff'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Hello, {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """- Say hello to the bot or a different user."""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello, {0.mention}~'.format(member))
        else:
            await ctx.send('You already said hello, {0.mention}'.format(member))
        self._last_member = member

    @commands.command(name='how-are-you')
    async def how_are_you(self, ctx, *, member: discord.Member = None):
        """- Ask how the bot is doing."""     
        await ctx.send(random.choice(cfg.HOW_ARE_YOU_RESPONSES))

                
