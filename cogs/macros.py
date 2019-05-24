import discord
from discord.ext import commands

import macros_list as mlist
import config as cfg

class Macros(commands.Cog, name='Macros'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='what-are-macros')
    async def desc_macros(self, ctx):
        """- What are macros?"""
        await ctx.send("Macros are commands that you can use to make the me say something specific, without typing it out yourself. (For example this is a macro.) There are also macros that listen for you to say certain things and then respond. You can list the macros with the `listMacros` command. _Note that some macros will delete your command after reading it._")

    @commands.command(name='listMacros')
    async def list_macros(self, ctx):
        """- Show available macros."""
        await ctx.send("The macro prefix is `{0}`. For example, type `{0}command.` Feel free to suggest macros.".format(cfg.MACRO_PREFIX)) 
        message_lines = ["`{name}`\t- {chelp} {cmd}\n".format(name=macro['name'], chelp=macro['help'], cmd='(command)' if macro['type'] == 'command' else '(listener)') for macro in mlist.MACROS if macro['help']]
        await ctx.send("".join(message_lines))

    @commands.command(name='listListeners')
    async def list_listeners(self, ctx):
        """- List my listeners and hidden commands."""
        await ctx.send("".join([l + '\n' for l in mlist.LISTENER_LIST]))

    @commands.Cog.listener()
    async def on_message(self, msg):
        for m in mlist.MACROS:
            if msg.content.startswith(cfg.MACRO_PREFIX + m['name']) or (m['name'].lower() in msg.content.lower() and m['type'] == 'listener'):
                await msg.channel.send(m['content'])
                if m['delete']:
                    await msg.delete()
                return

        if msg.content.startswith(cfg.MACRO_PREFIX):
            await msg.channel.send("I don't know that macro. Try asking @scitronboy to add it for you.")
