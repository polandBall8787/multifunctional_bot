from core.classes import Cog_Extension
from discord.ext import commands
import discord
import datetime

class Embeds(Cog_Extension):
  
  @commands.command()
  async def subscribe(self, ctx):
    embed=discord.Embed(title="訂閱!!", url="https://www.youtube.com/channel/UCi1elWTL51OYLQkhQYjAjPA", description="趕快訂閱!!!!!", color=0x515fc2, 
    timestamp=datetime.datetime.now())
    embed.set_author(name="余泓叡", url="https://www.youtube.com/channel/UCi1elWTL51OYLQkhQYjAjPA", icon_url="https://i.postimg.cc/hjzrh9cT/image.png")
    embed.set_thumbnail(url="https://i.postimg.cc/hjzrh9cT/image.png")
    embed.add_field(name="訂閱訂閱訂閱訂閱訂閱訂閱", value="快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!", inline=True)
    embed.set_footer(text="還在看什麼 快去訂閱阿！")
    await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Embeds(bot))