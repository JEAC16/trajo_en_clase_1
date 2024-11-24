import discord
from discord.ext import commands

permisos=discord.Intents.default()
permisos.message_content=True

bot=commands.Bot(command_prefix="/",intents=permisos)

@bot.event
async def on_ready():
    print(f"El bot llamado {bot.user} esta en linea para utilizar la funcion ca favor de utilizar del 1 al 10 cuanto gastas (cada unidad son 15 min con la llave abierta, igual con la funcion ce pero con 50 kilowatts por mes)")
@bot.command()
async def des(ctx,*,objeto:str):
    listaDescomposicion={
        "botella de plastico": 500,
        "chicle":10,
        "vidrio":5000,


    }


    objeto=objeto.lower()
    if objeto in listaDescomposicion:
        await ctx.send(f"El objeto llamado: {objeto} tarda en descomponerse aproximadamente{listaDescomposicion[objeto]} años")
    else:
        await ctx.send("No tengo información al respecto")
@bot.command()
async def ca(ctx,*,agua:str):
    listatiempodeagua={
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
    }
   
    if agua in listatiempodeagua:
        if agua <= 6:
            await ctx.send(f"El tiempo de uso de agua es {agua} y estas en un increible ahorro")
        elif agua <= 10 and agua <= 6:
            await ctx.send(f"El tiempo de uso de agua es {agua} y esta dentro de una media")
        else:
            await ctx.send("El tiempo de uso de agua en agua esta muy fuera de los normal intenta ahorrar un poco más")
@bot.command()
async def ce(ctx,*,energia:str):
    listawatts={
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        
         }
    if energia in listawatts:
        if energia <= 3:
            await ctx.send("si quiera utilizas electricidad???")
        if energia <= 6 and energia > 3:
            await ctx.send("tienes un uso normal y moderado sigue asi!!")
        if energia <= 10 and energia > 6:
            await ctx.send("intenta bajar el uso de la electricidad pues pasas por mucho lo recomendado")

        




bot.run("")
