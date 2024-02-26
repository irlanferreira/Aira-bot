import discord, tokens, os
from discord.ext import commands
from utils import ADM

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='<>', intents=discord.Intents.all())

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