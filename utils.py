from discord import app_commands
import discord
def ADM():
    async def verificar(interact:discord.Interaction):
        adm_cargo = interact.guild.get_role(1211707271508140072)
        if adm_cargo in interact.user.roles:
            return True
        else:
            await interact.response.send_message(f"Você não tem permissão para usar esse comando.", ephemeral=True)
            return False
    return app_commands.check(verificar)