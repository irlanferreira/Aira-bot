import discord, tokens, os
from discord.ext import commands
from utils import ADM
from cogs.ticket import Mensagem_Ticket_View

views = [Mensagem_Ticket_View]

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='<>', intents=discord.Intents.all())

    async def setup_hook(self):
        for view in views:
            bot.add_view(view())

bot = Bot()
async def carregar_cogs():
    for arquivo in os.listdir('./cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f"cogs.{arquivo[:-3]}")

@bot.event
async def on_ready():
    await carregar_cogs()
    sincs = len(await bot.tree.sync())
    print(f"{sincs} comandos sincronizados.")
# @ADM
# @bot.command()
# async def sync():
#     await bot.tree.sync()

bot.run(tokens.BOT_TOKEN)