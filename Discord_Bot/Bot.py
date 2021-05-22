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
  versionEmbed.set_author(name=" ")
  #Send embeded message
  await context.message.channel.send(embed=versionEmbed)

@Client.command(name='Author')
async def Author(context):
  #Create embeded message
  authorEmbed = discord.Embed(title="Author information", description=" ", color=0xff0000)
  authorEmbed.add_field(name="Author name", value="Manuel Capretta", inline=False)
  authorEmbed.add_field(name="Author discord", value="MC_2914#2113", inline=False)
  authorEmbed.set_footer(text="Nothing else to show here ;)")
   #Send embeded message
  await context.message.channel.send(embed=authorEmbed)

Client.run('TOKEN') #token