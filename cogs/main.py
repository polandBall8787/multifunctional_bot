import discord
from core.classes import Cog_Extension
from discord.ext import commands
import json
import random

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

class Main(Cog_Extension):
    
    @commands.command()
    @commands.has_role(int(config['bot_administrator']))
    async def 關機(self, ctx):
        await ctx.send('君要臣死，臣不得不死阿..... 再見了這個可怕的世界QAQ')
        await self.bot.close()

    @commands.command()
    @commands.has_role(int(config['bot_administrator']))
    async def 刪除(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    @commands.has_role(int(config['bot_administrator']))
    async def 隨機分組(self, ctx, teams: int, bob: int, t: int, role_name: str):
        online = []

        role = discord.utils.get(ctx.guild.roles, name=role_name)

        for member in ctx.guild.members:
            if str(member.status) == 'online' and not member.bot and role in member.roles:
                online.append(member.name)

        random_online = random.sample(online, k=bob)

        for squad in range(1, teams+1):
            if len(random_online) >= t:
                team = random.sample(random_online, k=t)
                await ctx.send(team)
                for name in team:
                    random_online.remove(name)
            else:
                await ctx.send("成員數量不足，無法組成更多隊伍。")

    @commands.command()
    async def 說(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))