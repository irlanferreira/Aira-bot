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
        await interact.response.send_message(view=Mensagem_Ticket_View())

class Mensagem_Ticket_View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(placeholder='Selecione uma categoria', custom_id='ticket_selecao', options=[
        discord.SelectOption(label='🚨Denúncia', value=1),
        discord.SelectOption(label='❓Dúvida', value=2),
        discord.SelectOption(label='🐞Reportar Bug', value=3)
        ])
    async def resposta_ticket_select(self, interaction:discord.Interaction, selecao:discord.ui.Select): 
        await interaction.response.send_message(f"{type(selecao.values[0])}")



async def setup(bot):
    await bot.add_cog(Ticket(bot))