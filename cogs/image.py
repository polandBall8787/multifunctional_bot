from core.classes import Cog_Extension
from discord.ext import commands
import discord
import random
import asyncio
import json


with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

class Image(Cog_Extension):

    @commands.command()
    async def image(self, ctx):
        options = ["poland", "a_c_cat", "noname", "random"]
        await ctx.send("請選擇你要的圖片:\n" + "\n".join(options))

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content in options

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send('一分鐘的時間都沒打完?你是在用屌打字嗎?')
        else:
            # 根據用戶的選擇發送對應的圖片
            if msg.content == "poland":
                images = discord.File(config['poland'])
            elif msg.content == "a_c_cat":
                images = discord.File(config['a_c_cat'])
            elif msg.content == "noname":
                images = discord.File(config['noname'])
            elif msg.content == "random":
                random_image = random.choice(config['all'])
                images = discord.File(random_image)
            await ctx.send(file=images)
            
# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Image(bot))