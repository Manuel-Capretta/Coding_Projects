import discord
from discord.ext import commands

Client = commands.Bot(command_prefix='--') #Get the command bot. Set prfic to '--'

@Client.command(name='version')
async def version(context):
  #Create Embeded message
  versionEmbed = discord.Embed(title="Current Version", description="All Versions", color=0xff0000)
  versionEmbed.add_field(name="Version Code:", value="Python 3.10", inline=False)
  versionEmbed.add_field(name="Bot Code:", value="1.0", inline=False)
  versionEmbed.set_footer(text="Versions do change from time to time")
  versionEmbed.set_author(name="My-first-bot")

  #Send embeded message
  await context.message.channel.send(embed=versionEmbed)

@Client.event
async def on_connect(message):
  if message.author == Client.user:
    return
  await message.channel.send('Hello!')
  
Client.run('ODQ1NjY1MjA0Nzc2MDc1MzU1.YKkRGA.7HW5edsjVMiLK1pcTNBPi4STjOE') #token