import discord
from discord.ext import commands
from discord import app_commands
from utils import ADM

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @app_commands.command()
    @ADM()
    async def enviar_botao_de_ticket(self, interact:discord.Interaction):
        await interact.response.send_message('a')

async def setup(bot):
    await bot.add_cog(Ticket(bot))