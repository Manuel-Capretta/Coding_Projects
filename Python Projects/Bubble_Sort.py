#Bubble Sort algorythm

def Bubble_sort(arr):
  n = len(arr)

  for i in range(n-1):
    for j in range(0, n-i-1):

      if(arr[j] > arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [13, 23, 5, 436, 2546, 435, 7, 4]

Bubble_sort(arr)                                #initialize Bubble sort

print(arr)