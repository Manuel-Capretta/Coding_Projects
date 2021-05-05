#include <stdio.h>

int main(){
    int c, n;
	int array[] = {1, 3, 4, 6, 4, 5, 343 ,34 ,765 ,9}; 
	int search = 5; //Number to search
    n = sizeof(array);  //length of array
	//Starting the Linear Search Algorithm.
	//Checking for the required element in the array.
	printf("\nStarting linear search…\n");
  	for (c = 0; c < n; c++){
		if (array[c] == search){ /* If the required element is found… */
		printf("%d is present at location %d.\n", search, c+1);
		break;
		}
  	}
	if (c == n){ /* if nothing was found…*/
		printf("%d isn't present in the array.\n", search);
	}
    return 0;
}