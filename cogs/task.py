import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

class Task(Cog_Extension):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.counter = 0

    async def time_task():
      await self.bot.wait_until_ready()
      self.channel = self.bot.get_channel(1247549967900348477)
      while not self.bot.is_closed():
        now_time = datetime.datetime.now().strftime('%H%M')
        with open('config.json', 'r', encoding='utf-8') as f:
          config = json.load(f)
        if now_time == config['time'] and self.counter == 0:
          await self.channel.send('時間到了!')
          await asyncio.sleep(1)
          self.counter = 1
        else:
          await asyncio.sleep(1)
          pass

    self.bg_task = self.bot.loop.create_task(time_task())

  @commands.command()
  @commands.has_role(int(config['bot_administrator']))
  async def 鬧鐘頻道(self, ctx, ch: int):
    self.channel = self.bot.get_channel(ch)
    await ctx.send(f'Set Channel: {self.channel.mention}')

  @commands.command()
  @commands.has_role(int(config['bot_administrator']))
  async def 設定時間(self, ctx, time):
    self.counter = 0
    with open('config.json', 'r', encoding='utf-8') as f:
      config = json.load(f)
    config['time'] = time
    with open('config.json', 'w', encoding='utf-8') as f:
      json.dump(config, f, indent=4)

async def setup(bot):
  await bot.add_cog(Task(bot))