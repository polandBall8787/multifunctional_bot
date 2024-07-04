from core.classes import Cog_Extension
from discord.ext import commands
import discord
import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

class Main(Cog_Extension):
    
    @commands.command()
    @commands.has_role(int(config['bot_administrator']))
    async def kill(self, ctx):
        await ctx.send('君要臣死，臣不得不死阿..... 再見了這個可怕的世界QAQ')
        await self.bot.close()

    @commands.command()
    async def repeat(self, ctx, *, message: str):
        await ctx.send(message)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))