import discord
from discord.ext import commands

Client = commands.Bot(command_prefix='--') #Get the command bot. Set prfic to '--'
tokenClient = discord.Client()

@Client.command(name='version')
async def version(context):
  #Create Embeded message
  versionEmbed = discord.Embed(title="Current Version", description="All Versions", color=0xff0000)
  versionEmbed.add_field(name="Version Code:", value="Python 3.10", inline=False)
  versionEmbed.add_field(name="Bot Code:", value="1.0", inline=False)
  versionEmbed.set_footer(text="Versions do change from time to time")
  versionEmbed.set_author(name=" ")

  #Send embeded message
  await context.message.channel.send(embed=versionEmbed)

@tokenClient.event
async def on_message(message):
   if message.content.startswith('pls traps'):
    await message.channel.send('No traps plz')

@tokenClient.event
async def on_connect():
   print("Bot ready")
  
Client.run('TOKEN') #token
tokenClient.run('TOKEN') #token