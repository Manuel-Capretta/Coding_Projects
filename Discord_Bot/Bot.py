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

@Client.command(name='Help')
async def Help(context):
  await context.message.channel.send(""" 
  Just type '--' and and the things (Code) you're searching for + the language. 
  (py = python / c = C)
  ex: --binary_search_py
  """)

@Client.command(name='binary_search_py')
async def Help(context):
  await context.message.channel.send("""
  Here you go: 

  # Iterative Binary Search
  # It returns index of x in given array arr if present, else returns -1

  def binary_search(arr, x):
      low = 0
      high = len(arr) - 1
      mid = 0

      while low <= high:
  
          mid = (high + low) // 2
  
          # If x is greater, ignore left half
          if arr[mid] < x:
              low = mid + 1
  
          # If x is smaller, ignore right half
          elif arr[mid] > x:
              high = mid - 1
  
          # means x is present at mid
          else:
              return mid
  
      # If we reach here, then the element was not present
      return -1
  
  
  # Test array
  arr = [ 2, 3, 4, 10, 40 ]
  x = 10
  
  # Function call
  result = binary_search(arr, x)
  
  if result != -1:
      print("Element is present at index", str(result))
  else:
      print("Element is not present in array")
  """)

@Client.command(name='binary_search_c')
async def Help(context):
  await context.message.channel.send("""
  Here you go: 

  // C program to implement iterative Binary Search
  #include <stdio.h>
  
  // A iterative binary search function. It returns
  // location of x in given array arr[l..r] if present,
  // otherwise -1
  int binarySearch(int arr[], int l, int r, int x)
  {
      while (l <= r) {
          int m = l + (r - l) / 2;
  
          // Check if x is present at mid
          if (arr[m] == x)
              return m;
  
          // If x greater, ignore left half
          if (arr[m] < x)
              l = m + 1;
  
          // If x is smaller, ignore right half
          else
              r = m - 1;
      }
  
      // if we reach here, then element was
      // not present
      return -1;
  }
  
  int main(void)
  {
      int arr[] = { 2, 3, 4, 10, 40 };
      int n = sizeof(arr) / sizeof(arr[0]);
      int x = 10;
      int result = binarySearch(arr, 0, n - 1, x);
      (result == -1) ? printf("Element is not present"
                              " in array")
                    : printf("Element is present at "
                              "index %d",
                              result);
      return 0;
  }
  """)

Client.run('Token') #token