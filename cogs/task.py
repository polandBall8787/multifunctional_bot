import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.counter = 0

    #async def interval():
    #  await self.bot.wait_until_ready()
    #  self.channel = self.bot.get_channel(1247549967900348477)
    #  while not self.bot.is_closed():
    #    await self.channel.send("HI i'm running")
    #    await asyncio.sleep(5)

    #self.bg_task = self.bot.loop.create_task(interval())

    async def time_task():
      await self.bot.wait_until_ready()
      self.channel = self.bot.get_channel(1247549967900348477)
      while not self.bot.is_closed():
        now_time = datetime.datetime.now().strftime('%H%M')
        with open('config.json', 'r', encoding='utf-8') as f:
          config = json.load(f)
        if now_time == config['time'] and self.counter == 0:
          await self.channel.send('Task Working!')
          await asyncio.sleep(1)
          self.counter = 1
        else:
          await asyncio.sleep(1)
          pass

    self.bg_task = self.bot.loop.create_task(time_task())

  @commands.command()
  async def set_channel(self, ctx, ch: int):
    self.channel = self.bot.get_channel(ch)
    await ctx.send(f'Set Channel: {self.channel.mention}')

  @commands.command()
  async def set_time(self, ctx, time):
    self.counter = 0
    with open('config.json', 'r', encoding='utf-8') as f:
      config = json.load(f)
    config['time'] = time
    with open('config.json', 'w', encoding='utf-8') as f:
      json.dump(config, f, indent=4)

async def setup(bot):
  await bot.add_cog(Task(bot))