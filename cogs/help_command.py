import discord
from core.classes import Cog_Extension
from core.embed_function import embeds
from discord.ext import commands
import asyncio
import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

class Help_Command(Cog_Extension):
  @commands.command()
  async def help(self, ctx):
    options = ["main", "image", "role", "task"]
    embed = embeds("help", "https://trr-embed.mystrikingly.com",
    "**這是一個help指令 (功能:指令檢查)** \n 以下是所有的指令的分類 以及各項分類的功能描述UwU", 0x3584e4, "bot", "https://trr-embed.mystrikingly.com",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png",
    "註:請選擇您要查看的指令類別OwO")

    embed.add_field(name=config['main'], 
    value="最基礎的指令",
    inline=False)

    embed.add_field(name=config['role'], 
    value="跟身份組取得有關的指令",
    inline=False)

    embed.add_field(name=config['task'], 
    value="鬧鐘(對 就只有這樣)",
    inline=False)

    embed.add_field(name="比較特殊的指令:",
    value="load(載入)<-須要機器人管理者身份組\n unload(移除)<-須要機器人管理者身份組\n reload(重新載入) <-須要機器人管理者身份組",
    inline=False)

    await ctx.send(embed=embed)

    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel and m.content in options

    try:
      msg = await self.bot.wait_for('message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
      await ctx.send('一分鐘的時間都沒打完?你是在用屌打字嗎?')
    else:
      if msg.content == "main":
        embed=embeds(config['main'], "https://trr-embed.mystrikingly.com",
        "**最基礎的指令** \n\n 以下是main底下的所有指令 以及各指令的功能描述UwU", 0x3584e4, "bot", "https://trr-embed.mystrikingly.com",
        "", 
        "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
        "註:請選擇您要使用的指令OwO")
        
        embed.add_field(name="shutdown", 
        value="**關閉機器人**\n(只有擁有**機器人管理者**的人能使用)",
        inline=False)

        embed.add_field(name="dels", 
        value="**刪除訊息**\n(後面要加上要**刪除的訊息的數量**、\n只有擁有**機器人管理者**的人能使用)",
        inline=False)

        embed.add_field(name="say", 
        value="**讓機器人幫你說話**",
        inline=False)

        embed.add_field(name="random_team", 
        value="**隨機分組** \n(總共要輸入三個參數  1.最多人數 2.分成幾對 3.每組幾人\n註:只有擁有**在線玩家身份組\n**並且**在線**的用戶才會被列入分組選項中)",
        inline=False)

        await ctx.send(embed=embed)

      if msg.content == "role":
        embed=embeds(config['role'], "https://trr-embed.mystrikingly.com",
        "**跟身份組有關的指令** \n\n 以下是role底下的所有指令 以及各指令的功能描述UwU", 0x3584e4, "bot", "https://trr-embed.mystrikingly.com",
        "", 
        "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
        "註:請選擇您要使用的指令OwO")
        
        embed.add_field(name="claim_role", 
        value="**領取身份組**\n(只有**旁觀者**、**在線玩家**可以領取)",
        inline=False)

        embed.add_field(name="remove_online_player_role", 
        value="**移除在線玩家身份組**",
        inline=False)

        await ctx.send(embed=embed)
        
      if msg.content == "task":
        embed=embeds(config['task'], "https://trr-embed.mystrikingly.com",
        "**鬧鐘** \n\n 以下是task底下的所有指令 以及各指令的功能描述UwU", 0x3584e4, "bot", "https://trr-embed.mystrikingly.com",
        "", 
        "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
        "註:請選擇您要使用的指令OwO")
        
        embed.add_field(name="task_time", 
        value="**鬧鐘時間設定**\n(後面必須輸入時間 例:0532(24小時制)、只有擁有**機器人管理者**的人能使用)",
        inline=False)

        embed.add_field(name="task_channel", 
        value="**鬧鐘頻道設定**\n(後面必須頻道ID 例:123456789、只有擁有**機器人管理者**的人能使用)",
        inline=False)

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help_Command(bot))