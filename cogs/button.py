import discord
from discord.ext import commands

class button(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="click me", style=discord.ButtonStyle.gray)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("you click me :]")
    
    @discord.ui.button(label="t my rr", style=discord.ButtonStyle.green)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("you t my rr :)")
    
    @discord.ui.button(label="t he rr", style=discord.ButtonStyle.red)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("you t noname rr :)")
        
class Menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):

        view = button()
        view.add_item(discord.ui.Button(label="URL Button", style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=82d9s8D6XE4"))
        await ctx.reply(view=view)

async def setup(bot):
  await bot.add_cog(Menu(bot))
