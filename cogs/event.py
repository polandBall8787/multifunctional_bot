from core.classes import Cog_Extension
from discord.ext import commands
import discord
import json

with open('config.json', 'r', encoding='utf-8') as f:
  config = json.load(f)

class Event (Cog_Extension):

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.bot.get_channel(int(config['welcome']))
    await channel.send(f'{member.mention}被黑洞吸進來了!')

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel(int(config['leave']))
    await channel.send(f'{member.mention}被白洞吐出去了! 我們懷念他 :_(!')

  @commands.Cog.listener()
  async def on_message(self, msg):
    keyword = ['Hello', 'hello', 'HELLO', 'Hi', 'HI', 'hi']
    if msg.author == self.bot.user:
      return

    if msg.content in keyword:
      await msg.channel.send('hi')

async def setup(bot: commands.Bot):
  await bot.add_cog(Event(bot))