import discord
from discord.ext import commands
import asyncio
import json
import os

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='`', intents=intents)

@bot.event
async def on_ready():
  print("[ bot is online !!!]")
  play_bot = bot.get_channel(int(config['play_bot']))
  await play_bot.send("我復活啦!")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('你的社會地位太低啦!哈哈哈 所以你沒辦法使用這個指令XD')
    else:
        await ctx.send(f'damn! 程式出錯了! 錯誤資訊：{error}')
        raise error

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(config['TOKEN'])

if __name__ == "__main__":
    asyncio.run(main())