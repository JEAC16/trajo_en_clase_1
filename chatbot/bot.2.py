import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot= commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready(): 
    print(f"Se inicio el bot{bot.user}")
@bot.command()
async def hola(ctx):
    await ctx.send(f"buenos dias o cualquier hora en la que este mi querido estimado el dia de hoy se ve excelente me llamo {bot.user} a sus ordenes ")
@bot.command()
async def adios(ctx):
    await ctx.send(f"que le vaya muy bien en la increible aventura llamada vida y espero que se recupere del mundo del internet lo veo la proxima vez se despide {bot.user}")
bot.run()
