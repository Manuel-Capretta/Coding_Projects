#include <stdio.h>
#include <math.h>
#include <stdbool.h>

void InSor();

int main(void) {
	int a;
	int n = 10; //length of array (only this amount of nubers in the array get sorted)
	int arr[] = {1, 2, 28, 4, 50, 6, 7, 8, 9, 10}; //array itself
	a = 1;
	if(a == 1){ //Sorting by comparing sorted numbers in front 
		printf("Start Sorting… \n");
		InSor(arr, n);
	} else if(a == 2){

	}
	return 0;
}

void InSor(int arr[], int n){
	int i, key, j; 
/*------------------------------------------------*/
    for (i = 1; i < n; i++){ 
        key = arr[i]; 
        j = i - 1; 
        /* Move elements of arr[0..i-1], that are 
          greater than key, to one position ahead 
          of their current position */
        while (j >= 0 && arr[j] > key){ 
            arr[j + 1] = arr[j]; 
            j = j - 1; 
        } 
        arr[j + 1] = key; 
    } 
/*------------------------------------------------*/
	printf("{ ");
	for (i = 0; i < n; i++){
        printf("%d ", arr[i]); 
	}
	printf("}");
	printf("\nDone!\n");
}