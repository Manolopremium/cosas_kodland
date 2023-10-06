import discord
from discord.ext import commands



from bot_logic import gen_pass



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('Hemos iniciado sesión como {bot.user}')

@bot.command
async def hello(ctx):
        await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run("Token")
