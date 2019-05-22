import discord
from discord.ext import commands

import config as cfg

async def is_bot_admin(ctx):
    isadmin = ctx.author.id == 563490372836130817 or\
        len([r for r in ctx.author.roles if r.name in cfg.BOT_ADMIN_ROLES]) > 0

    if not isadmin:
        await ctx.send("Do you have permission to execute that command? :thinking:")
        return False
    return True
        

