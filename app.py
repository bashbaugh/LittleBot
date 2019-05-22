# Jimbo Discord Bot
# Written by Benjamin Ashbaugh and contributors
# https://github.com/scitronboy/Jimbo
# Licensed under the MIT license.

import random
from time import sleep
import importlib

import discord
from discord.ext import commands
import logging

import config as cfg
from util import userUtils

logger = logging.getLogger('discord')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
logger.setLevel(logging.INFO)
fhandler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
fhandler.setFormatter(formatter)
shandler = logging.StreamHandler()
shandler.setFormatter(formatter)

logger.addHandler(fhandler)
logger.addHandler(shandler)

bot = commands.Bot(command_prefix='--')

@bot.event
async def on_ready():
    logger.info('We have logged in as {0.user}'.format(bot))
    game = discord.Game(random.choice(cfg.BOT_ACTIVITIES))
    await bot.change_presence(status=discord.Status.online, activity=game)


for cog in cfg.COMMAND_COGS:
    bot.add_cog(cog['class'](bot))

bot.run(cfg.APP_TOKEN)
