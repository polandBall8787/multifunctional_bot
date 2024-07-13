from core.classes import Cog_Extension
from discord.ext import commands
import discord
import random
import asyncio
import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

class Role(Cog_Extension):

    @commands.command()
    async def 領取身份(self, ctx):
        options = ["旁觀者", "在線玩家"]
        await ctx.send("請選擇你要的身份:\n" + "\n".join(options))
        user = ctx.author
        role_id = 1093099222712201226  # 替換為你想要新增的身份組的 ID
        role = ctx.guild.get_role(role_id)
        role_id_two = 1261583888728457217  # 替換為你想要新增的身份組的 ID
        roletwo = ctx.guild.get_role(role_id_two)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content in options

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send('一分鐘的時間都沒打完?你是在用屌打字嗎?')
        else:

            if msg.content == "旁觀者":
                await user.add_roles(role)
                await ctx.send(f"已將身份組 {role.name} 新增給 {user.name}。")
            elif msg.content == "在線玩家":
                await user.add_roles(roletwo)
                await ctx.send(f"已將身份組 {roletwo.name} 新增給 {user.name}。")

    @commands.command()
    async def 移除身份_在線玩家(self, ctx):
        role_id = 1261583888728457217  # 要移除的身份組的ID
        role = ctx.guild.get_role(role_id)
        user = ctx.author

        await user.remove_roles(role)
        await ctx.send(f"已從 {user.name} 移除身份組 {role.name}。")

async def setup(bot: commands.Bot):
    await bot.add_cog(Role(bot))