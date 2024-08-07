import discord
from core.classes import Cog_Extension
from core.embed_function import embeds
from discord.ext import commands

class HomeButton(discord.ui.View):
  def __init__(self):
    super().__init__()

  @discord.ui.button(label="回主頁", style=discord.ButtonStyle.primary)
  async def gohome(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds("help", "https://trr-embed.mystrikingly.com",
    "**這是一個help指令 (功能:指令檢查)** \n 以下是所有的指令的分類 以及各項分類的功能描述UwU", 0x3584e4, "bot",
    "https://trr-embed.mystrikingly.com",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png",
    "註:請選擇您要查看的指令類別OwO")

    embed.add_field(name='main', 
    value="最基礎的指令",
    inline=False)

    embed.add_field(name='role', 
    value="跟身份組取得有關的指令",
    inline=False)

    embed.add_field(name='task', 
    value="鬧鐘(對 就只有這樣)",
    inline=False)

    embed.add_field(name="比較特殊的指令:",
    value="load(載入)<-須要機器人管理者身份組\n unload(移除)<-須要機器人管理者身份組\n reload(重新載入) <-須要機器人管理者身份組",
    inline=False)

    await interaction.response.send_message(embed=embed)

class MainButton(discord.ui.View):
  def __init__(self):
    super().__init__()

  @discord.ui.button(label="say 的詳細資訊", style=discord.ButtonStyle.success)
  async def say(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('say', "https://trr-embed.mystrikingly.com",
    "**讓機器人幫你說話** \n\n 以下是say的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="**讓機器人幫你說話**",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`say**後面加上你要讓機器人幫你說的話\n(例:`say you are SB)",
    inline=False)

    view = HomeButton()
    await interaction.response.send_message(embed=embed, view=view)

  @discord.ui.button(label="random_team 的詳細資訊", style=discord.ButtonStyle.primary)
  async def random_team(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('random_team', "https://trr-embed.mystrikingly.com",
    "**隨機分組** \n\n 以下是random_team的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="**在玩遊戲時可以隨機分組**",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`random_team**後面加上三個必要的參數\n1.**最多人數** 2.**分成幾對** 3.**每組幾人**\n註:只有擁有**在線玩家身份組\n**並且**在線**的用戶才會被列入分組選項中\n(例:`**random_team 20 4 5** *<=20人中分成4對每對5人*)",
    inline=False)

    await interaction.response.send_message(embed=embed)
        
  @discord.ui.button(label="dels 的詳細資訊", style=discord.ButtonStyle.danger)
  async def dels(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('dels', "https://trr-embed.mystrikingly.com",
    "**批量刪除訊息** \n\n 以下是dels的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="**讓機器人幫你說話**(只有擁有**機器人管理者**的人能使用)",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`dels**後面加上你要刪除的訊息的數量\n(例:**`dels 50000000000** \n註:各位管理員請勿這樣操作機器人 不然會崩潰!!!)",
    inline=False)

    await interaction.response.send_message(embed=embed)

  @discord.ui.button(label="shutdown 的詳細資訊", style=discord.ButtonStyle.danger)
  async def shutdown(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('shutdown', "https://trr-embed.mystrikingly.com",
    "**關機** \n\n 以下是shutdown的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="**關閉機器人**(只有擁有**機器人管理者**的人能使用)",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`shutdown**就可以了",
    inline=False)

    await interaction.response.send_message(embed=embed)

class RoleButton(discord.ui.View):
  def __init__(self):
    super().__init__()

  @discord.ui.button(label="claim_role 的詳細資訊", style=discord.ButtonStyle.primary)
  async def claim_role(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('claim_role', "https://trr-embed.mystrikingly.com",
    "**領取身分組** \n\n 以下是claim_role的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="**領取身分組**",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`claim_role**就可以了",
    inline=False)

    await interaction.response.send_message(embed=embed)

  @discord.ui.button(label="remove_online_player_role 的詳細資訊", style=discord.ButtonStyle.danger)
  async def remove_online_player_role(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('remove_online_player_role', "https://trr-embed.mystrikingly.com",
    "**移除再現玩家身分組** \n\n 以下是remove_online_player_role的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="移除: **在線玩家身份組**",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`remove_online_player_role**就可以了",
    inline=False)

    await interaction.response.send_message(embed=embed)

class TaskButton(discord.ui.View):
  def __init__(self):
    super().__init__()

  @discord.ui.button(label="task_time 的詳細資訊", style=discord.ButtonStyle.primary)
  async def task_time(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('task_time', "https://trr-embed.mystrikingly.com",
    "**鬧鐘** \n\n 以下是task_time的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="這就只是一個鬧鐘我是能介紹什麼？(只有擁有**機器人管理者**的人能使用)",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`task_time**並加上你要設定的時間\n(例:`task_time 1660 註:時間的格式是:%H%M 例:17:01 = 1701)",
    inline=False)

    await interaction.response.send_message(embed=embed)

  @discord.ui.button(label="task_channel 的詳細資訊", style=discord.ButtonStyle.primary)
  async def task_channel(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('task_channel', "https://trr-embed.mystrikingly.com",
    "**鬧鐘頻道** \n\n 以下是task_time的指令使用方式 以及指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "趕快去試試吧!")

    embed.add_field(name="功能", 
    value="設定鬧鐘時間到時出現訊息的頻道(只有擁有**機器人管理者**的人能使用)",
    inline=False)

    embed.add_field(name="使用方法",
    value="輸入:**`task_channel**並加上你要的頻道\n(例:`task_channel 1089429892661260309",
    inline=False)

    await interaction.response.send_message(embed=embed)


class button(discord.ui.View):
  def __init__(self):
    super().__init__()

  @discord.ui.button(label="main", style=discord.ButtonStyle.primary)
  async def main(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('main', "https://trr-embed.mystrikingly.com",
    "**最基礎的指令** \n\n 以下是main底下的所有指令 以及各指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
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

    view = MainButton()
    await interaction.response.send_message(embed=embed, view=view)
        
    
  @discord.ui.button(label="role", style=discord.ButtonStyle.primary)
  async def role(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('role', "https://trr-embed.mystrikingly.com",
    "**跟身份組有關的指令** \n\n 以下是role底下的所有指令 以及各指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "註:請選擇您要使用的指令OwO")
        
    embed.add_field(name="claim_role", 
    value="**領取身份組**\n(只有**旁觀者**、**在線玩家**可以領取)",
    inline=False)

    embed.add_field(name="remove_online_player_role", 
    value="**移除在線玩家身份組**",
    inline=False)
    view = RoleButton()
    await interaction.response.send_message(embed=embed, view=view)
    
  @discord.ui.button(label="task", style=discord.ButtonStyle.primary)
  async def task(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.message.delete()
    embed=embeds('task', "https://trr-embed.mystrikingly.com",
    "**鬧鐘** \n\n 以下是task底下的所有指令 以及各指令的功能描述UwU", 0x3584e4, "bot", 
    "https://trr-embed.mystrikingly.com","",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png", 
    "註:請選擇您要使用的指令OwO")
        
    embed.add_field(name="task_time", 
    value="**鬧鐘時間設定**\n(後面必須輸入時間 例:0532(24小時制)、只有擁有**機器人管理者**的人能使用)",
    inline=False)

    embed.add_field(name="task_channel", 
    value="**鬧鐘頻道設定**\n(後面必須頻道ID 例:123456789、只有擁有**機器人管理者**的人能使用)",
    inline=False)

    view = TaskButton()
    await interaction.response.send_message(embed=embed, view=view)

class Help_Command(Cog_Extension):
  @commands.command()
  async def help(self, ctx):
    embed=embeds("help", "https://trr-embed.mystrikingly.com",
    "**這是一個help指令 (功能:指令檢查)** \n 以下是所有的指令的分類 以及各項分類的功能描述UwU", 0x3584e4, "bot",
    "https://trr-embed.mystrikingly.com",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png",
    "https://i.ibb.co/XXGNHbN/multifunctional-bot.png",
    "註:請選擇您要查看的指令類別OwO")

    embed.add_field(name='main', 
    value="最基礎的指令",
    inline=False)

    embed.add_field(name='role', 
    value="跟身份組取得有關的指令",
    inline=False)

    embed.add_field(name='task', 
    value="鬧鐘(對 就只有這樣)",
    inline=False)

    embed.add_field(name="比較特殊的指令:",
    value="load(載入)<-須要機器人管理者身份組\n unload(移除)<-須要機器人管理者身份組\n reload(重新載入) <-須要機器人管理者身份組",
    inline=False)

    view = button()
    await ctx.send(embed=embed, view=view)

async def setup(bot: commands.Bot):
  await bot.add_cog(Help_Command(bot))