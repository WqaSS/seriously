# main.py
import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
import logging
from discord import Activity, ActivityType

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

bot = commands.Bot(command_prefix=prefix, intents=intents)

# Rich Presence
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=ActivityType.watching, name="seriously.tk・;help"))
    logger.info(f'Bot conectado como {bot.user}')
    try:
        await load_cogs()
    except Exception as e:
        logger.error(f"Error al cargar cogs: {e}")

# Cargar cogs automáticamente
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                logger.info(f"Cog cargado: {filename[:-3]}")
            except Exception as e:
                logger.error(f"Error al cargar {filename[:-3]}: {e}")

# Manejo de errores generales
@bot.event
async def on_error(event, *args, **kwargs):
    logger.error(f"Error en el evento {event}: {str(args)}", exc_info=True)

if __name__ == "__main__":
    try:
        bot.run(token)
    except Exception as e:
        logger.critical(f"Error al iniciar el bot: {e}")