import discord
import datetime

def embeds(title, indexurl, description, color, username, userurl, usericon, icon_url, footertext):
  embed=discord.Embed(title=title, url=indexurl, description=description, color=color, 
  timestamp=datetime.datetime.now())
  embed.set_author(name=username, url=userurl, icon_url=usericon)
  embed.set_thumbnail(url=icon_url)
  embed.set_footer(text=footertext)
  return embed