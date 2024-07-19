import discord
from core.classes import Cog_Extension
from core.embed_function import embeds
from discord.ext import commands

class Embeds(Cog_Extension):

  @commands.command()
  async def subscribe(self, ctx):
    embed=embeds("訂閱!!", "https://www.youtube.com/channel/UCi1elWTL51OYLQkhQYjAjPA",
    "趕快訂閱!!!!!", 0x515fc2, "余泓叡", "https://www.youtube.com/channel/UCi1elWTL51OYLQkhQYjAjPA",
    "https://i.postimg.cc/hjzrh9cT/image.png", 
    "https://i.postimg.cc/hjzrh9cT/image.png",
    "還在看什麼 快去訂閱阿！")
    embed.add_field(name="訂閱訂閱訂閱訂閱訂閱訂閱", 
    value="快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!",
    inline=True)
    await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Embeds(bot))