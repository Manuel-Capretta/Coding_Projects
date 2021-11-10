#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int main(void){
  int num = 8;
  int arr[] = {2, 5, 7, 15, 3, 4};
  int solArr[2]; 
  /*Your Code*/
  for(int i = 0; i < sizeof(arr); i++){
    for(int j = 1; j < sizeof(arr); j++ ){
      if (arr[i] + arr[j] == num) {
        solArr[0] = arr[i];
        solArr[1] = arr[j];
      }
    }
  }

  printf("%d + %d = %d", solArr[0], solArr[1], num);

}