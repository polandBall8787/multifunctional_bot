import discord
from core.classes import Cog_Extension
from discord.ext import commands
import datetime

def embeds(title, indexurl, description, color, username, userurl, usericon, icon_url, fieldname, fieldvalue, footertext):
  embed=discord.Embed(title=title, url=indexurl, description=description, color=color, 
  timestamp=datetime.datetime.now())
  embed.set_author(name=username, url=userurl, icon_url=usericon)
  embed.set_thumbnail(url=icon_url)
  embed.add_field(name=fieldname, value=fieldvalue, inline=True)
  embed.set_footer(text=footertext)
  return embed

class Embeds(Cog_Extension):

  @commands.command()
  async def 訂閱(self, ctx):
    embed=embeds("訂閱!!", "https://www.youtube.com/channel/UCi1elWTL51OYLQkhQYjAjPA",
"趕快訂閱!!!!!", 0x515fc2, "余泓叡", "https://www.youtube.com/channel/UCi1elWTL51OYLQkhQYjAjPA",
"https://i.postimg.cc/hjzrh9cT/image.png", 
"https://i.postimg.cc/hjzrh9cT/image.png", 
"訂閱訂閱訂閱訂閱訂閱訂閱",
"快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!快去訂閱!",
"還在看什麼 快去訂閱阿！")
    await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Embeds(bot))