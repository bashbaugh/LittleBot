import random
import urllib.request
import json
import discord
from discord.ext import commands

import config as cfg

class Fun(commands.Cog, name='Memes'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        """Respond to 'latest xkcd' or 'xkcd #x'"""
        if "latest xkcd" in message.content:
            # https://xkcd.com/json.html
            latestURL = "https://xkcd.com/info.0.json"
            req = urllib.request.Request(latestURL)
            data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
            await message.channel.send('"' + data['alt'] + '": ' + data['img'])

        if "xkcd #" in message.content:
            before, kw, after = message.content.partition('xkcd #')
            num = after.split(' ')[0]
            URL =  "https://xkcd.com/{}/info.0.json".format(num)
            req = urllib.request.Request(URL)
            try:
                data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
                await message.channel.send(str(num) + ', "' + data['alt'] + '" ' + data['img'])
            except urllib.error.HTTPError:
                await message.channel.send("HTTP error. Are you sure that's a valid id? To get an xkcd, please type `xkcd #x`, where x is the xkcd comiic id (a number)")

    @commands.command(name='Fun')
    async def getmeme(self, ctx, meme_type=None):
        """[google] - Fetch a meme from the internet."""
        message = ""
        if meme_type is None:
            # message += "Meme type not specified. Defaulting to `{}` ".format(cfg.DEFAULT_MEME_TYPE)
            meme_type = cfg.DEFAULT_MEME_TYPE

        if meme_type == 'google':
            q = random.choice(cfg.GOOGLE_MEME_SEARCH_QUERIES)
            num = 1
            start = random.randint(1, 100)
            api_url = "https://www.googleapis.com/customsearch/v1?searchType=image&imgSize=medium&q={q}&num={num}&start={start}&key={key}&cx={cx}"
            formatted_url = api_url.format(q=q, num=num, start=start, key=cfg.GOOGLE_CUSTOM_SEARCH_KEY, cx=cfg.GOOGLE_CUSTOM_SEARCH_ID)
            req = urllib.request.Request(formatted_url)
            res = urllib.request.urlopen(req).read()
            data = json.loads(res.decode('utf-8'))
            image_url = data['items'][0]['link']
            message += image_url
             
        else:
            message +=" `{}` is not a supported meme type. ".format(meme_type)

        await ctx.send(message)

        
