#Dependencies/Modules (whatever you like to call them i call them modules) START
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio 
#Deps/Modules END

#Variables START
bot = discord.Client()
prefix = commands.Bot(command_prefix = "A-")
botversion = "vBETA-2 GitHubRelease"
botid = "471639801314148362"
owner = "Alej0hio"
botinfo = discord.AppInfo
ownerID = "315843700490240002"
#Variables END

#Events START
@bot.event
async def on_ready():
    print ("MY BOT IS READY")
    print (botid)
    print ("Alej0hio")

@bot.event
async def on_error():
    print("Whoops, an error accoured! Please report this on the github page.")


    

@bot.event
async def on_message(message):
    if message.content.upper().startswith('A-PING'):
        userID = message.author.id
        await bot.send_message(message.channel, "Pong!")  
    if message.content.upper().startswith('A-SAY'):
          args = message.content.split (" ")
          await bot.send_message(message.channel, "%s" % (args[1:])) 
    if message.content.upper().startswith('A-VERSION'):
        await bot.send_message(message.channel, botversion)
    if message.content.upper().startswith('A-CREDIT'):
        await bot.send_message(message.channel, "Alej0hio#5306 for code, https://alej0hio.blogspot.com , https://github.com/Alej0hio , https://discord.gg/fsmBbhG .This bot uses discord.py. https://github.com/Rapptz/discord.py Discord.py is made by Rapptz. ")
    if message.content.upper().startswith('A-MODULES'):
        await bot.send_message(message.channel,"discord.py,async. thats all right now")
    if message.content.upper().startswith('A-BOTLANGUAGE'):
        await bot.send_message(message.channel,"Alej0hibot is made in Python! https://python.org for more info")
    if message.content.upper().startswith('A-TEST'):
        await bot.send_message(message.channel,":white_check_mark: The bot responded to the command, it just works:tm:!")
    if message.content.upper().startswith('A-CORNIER'):
        await bot.send_message(message.channel,"Very cool guy")
    if message.content.upper().startswith('A-LARSENV'):
        await bot.send_message(message.channel,"Guy who works for https://rc24.xyz , https://mariocube.xyz , is admin of https://wiki.mariocube.xyz. Very cool dude indeed.")
    if message.content.upper().startswith('A-OSC'):
        await bot.send_message(message.channel,"Can we not use soap we should use shampoo!")
    if message.content.upper().startswith('A-RC24'):
        await bot.send_message(message.channel,"cmOC wHeN?????+++?????111!1!!!!!")
    if message.content.upper().startswith('A-FUNNY'):
        await bot.send_message(message.channel,"Oh my god when he falled I threw up my coke :laughing: https://cdn.discordapp.com/attachments/426478571389976581/471963769707167754/ohaio.gif")
    if message.content.upper().startswith('A-INFO'):
        await bot.send_message(message.channel, )  
#Events END



#most important part 
bot.run("put in your discord bots token here.")
