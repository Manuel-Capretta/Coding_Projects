#include <stdio.h>
  
int binarySearch(int arr[], int n, int x);

int main(void){
   int arr[] = {2, 3, 4, 10, 40};
   int n = sizeof(arr)/ sizeof(arr[0]);
   int x = 10;
   int result = binarySearch(arr, n, x);
   if(result == -1){ 
		 printf("Element is not present in array");
	 } else {
		printf("Element is present at index %d", result);
	 }           
   return 0;
}

int binarySearch(int arr[], int n, int x){
  
	int l = 0;
	int r = n-1;
	
	while(l <= r){
    int m = l + (r-l)/2;				//middle
    
    if(arr[m] == x){					//if x is present at mid
        return m;  
		} else if(arr[m] < x){ 			//if x is present in the right half
        l = m + 1;
		} else if(arr[m] > x){			//if it is present in the left half
         r = m - 1; 
		}	
  }
  //element was not present
  return -1; 
}