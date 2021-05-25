import discord
from discord.ext import commands

Client = commands.Bot(command_prefix='--') #Get the command bot. Set prfic to '--'










@Client.command(name='version')
async def version(context):
  #Create Embeded message
  versionEmbed = discord.Embed(title="Current Version", description="All Versions", color=0xff0000)
  versionEmbed.add_field(name="Code Version:", value="Python 3.10", inline=False)
  versionEmbed.add_field(name="Bot Version:", value="1.0", inline=False)
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

@Client.command(name='Syntax')
async def Syntax(context):
  await context.message.channel.send(""" 
  -- + _algorithm_ + language
  (py = python / c = C / cs = c# / j = Java / js = javascript)
  ex: --binary_search_py

  >Type:--help [Command] for the right syntax

  Note: All spaces MUST be replaced with an UNDERSCORE !!!
  """)










#---------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------
@Client.command(name='binary_search_cs')
async def Help(context):
  await context.message.channel.send("""
  // C# implementation of iterative Binary Search
  using System;
  
  class GFG {
      // Returns index of x if it is present in arr[],
      // else return -1
      static int binarySearch(int[] arr, int x)
      {
          int l = 0, r = arr.Length - 1;
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
  
      // Driver method to test above
      public static void Main()
      {
          int[] arr = { 2, 3, 4, 10, 40 };
          int n = arr.Length;
          int x = 10;
          int result = binarySearch(arr, x);
          if (result == -1)
              Console.WriteLine("Element not present");
          else
              Console.WriteLine("Element found at "
                                + "index " + result);
      }
  }
  """)
#---------------------------------------------------------------------------------
@Client.command(name='binary_search_j')
async def Help(context):
  await context.message.channel.send("""
  // Java implementation of iterative Binary Search
  class BinarySearch {
      // Returns index of x if it is present in arr[],
      // else return -1
      int binarySearch(int arr[], int x)
      {
          int l = 0, r = arr.length - 1;
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
  
      // Driver method to test above
      public static void main(String args[])
      {
          BinarySearch ob = new BinarySearch();
          int arr[] = { 2, 3, 4, 10, 40 };
          int n = arr.length;
          int x = 10;
          int result = ob.binarySearch(arr, x);
          if (result == -1)
              System.out.println("Element not present");
          else
              System.out.println("Element found at "
                                + "index " + result);
      }
  }
  """)
#---------------------------------------------------------------------------------
@Client.command(name='binary_search_js')
async def Help(context):
  await context.message.channel.send("""
  // Program to implement recursive Binary Search in Javascript
  // A recursive binary search function. It returns
  // location of x in given array arr[l..r] is present,
  // otherwise -1
  function binarySearch(arr, l, r, x)
  {
      if (r >= l) {
          mid = l + Math.floor((r - l) / 2);
    
          // If the element is present at the middle
          // itself
          if (arr[mid] == x)
              return mid;
    
          // If element is smaller than mid, then
          // it can only be present in left subarray
          if (arr[mid] > x)
              return binarySearch(arr, l, mid - 1, x);
  
          // Else the element can only be present
          // in right subarray
          return binarySearch(arr, mid + 1, r, x);
      }
    
      // We reach here when element is not
      // present in array
      return -1;
  }
  
      arr =new Array(2, 3, 4, 10, 40);
      x = 10;
      n = arr.length;
      result = binarySearch(arr, 0, n - 1, x);
      
  (result == -1) ? document.write("Element is not present in array")
                : document.write ("Element is present at index " + result);
  """)
#---------------------------------------------------------------------------------
@Client.command(name='insertion_sort_py')
async def Help(context):
  await context.message.channel.send("""
    # Python program for implementation of Insertion Sort
 
# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
  """)
#---------------------------------------------------------------------------------
@Client.command(name='insertion_sort_c')
async def Help(context):
  await context.message.channel.send("""
# Python program for implementation of Insertion Sort
 
# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
  """)
#---------------------------------------------------------------------------------
@Client.command(name='insertion_sort_cs')
async def Help(context):
  await context.message.channel.send("""
// C# program for implementation of Insertion Sort
using System;
 
class InsertionSort {
 
    // Function to sort array
    // using insertion sort
    void sort(int[] arr)
    {
        int n = arr.Length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;
 
            // Move elements of arr[0..i-1],
            // that are greater than key,
            // to one position ahead of
            // their current position
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
 
    // A utility function to print
    // array of size n
    static void printArray(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n; ++i)
            Console.Write(arr[i] + " ");
 
        Console.Write("\n");
    }
 
    // Driver Code
    public static void Main()
    {
        int[] arr = { 12, 11, 13, 5, 6 };
        InsertionSort ob = new InsertionSort();
        ob.sort(arr);
        printArray(arr);
    }
}
  """)
#---------------------------------------------------------------------------------
@Client.command(name='insertion_sort_j')
async def Help(context):
  await context.message.channel.send("""
// Java program for implementation of Insertion Sort
class InsertionSort {
    /*Function to sort array using insertion sort*/
    void sort(int arr[])
    {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;
 
            /* Move elements of arr[0..i-1], that are
               greater than key, to one position ahead
               of their current position */
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
 
    /* A utility function to print array of size n*/
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
 
        System.out.println();
    }
 
    // Driver method
    public static void main(String args[])
    {
        int arr[] = { 12, 11, 13, 5, 6 };
 
        InsertionSort ob = new InsertionSort();
        ob.sort(arr);
 
        printArray(arr);
    }
}
  """)
#---------------------------------------------------------------------------------
@Client.command(name='insertion_sort_js')
async def Help(context):
  await context.message.channel.send("""
// Javascript program for insertion sort 
   
// Function to sort an array using insertion sort
function insertionSort(arr, n) 
{ 
    let i, key, j; 
    for (i = 1; i < n; i++)
    { 
        key = arr[i]; 
        j = i - 1; 
   
        /* Move elements of arr[0..i-1], that are 
        greater than key, to one position ahead 
        of their current position */
        while (j >= 0 && arr[j] > key)
        { 
            arr[j + 1] = arr[j]; 
            j = j - 1; 
        } 
        arr[j + 1] = key; 
    } 
} 
   
// A utility function to print an array of size n 
function printArray(arr, n) 
{ 
    let i; 
    for (i = 0; i < n; i++) 
        document.write(arr[i] + " "); 
    document.write("<br>");
} 
   
// Driver code
    let arr = [12, 11, 13, 5, 6 ]; 
    let n = arr.length; 
   
    insertionSort(arr, n); 
    printArray(arr, n); 
  """)
#---------------------------------------------------------------------------------
@Client.command(name='_js')
async def Help(context):
  await context.message.channel.send("""

  """)





Client.run('TOKEN') #token