/*find the two numbers in the array that add up to num*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int main(void){
  int num = 9;
  int arr[] = {2, 5, 7, 15, 3, 4};
  int solArr[2]; 
  bool stopIt_getSomeHelp = false; //breaks both loops

  /*Your Code*/
  for(int i = 0; i < sizeof(arr); i++){
    //Breaks both loops
    if(stopIt_getSomeHelp){
      break;
    } else {
      for(int j = i+1; j < sizeof(arr); j++){
        if (arr[i] + arr[j] == num) {
          solArr[0] = arr[i];
          solArr[1] = arr[j];
          printf("\n%d + %d = %d", solArr[0], solArr[1], num);
          stopIt_getSomeHelp = true;
        } 
      }
      //If num isn't in there
      if(i == 5){
        printf("\nAin't in there mate");
        stopIt_getSomeHelp = true;
      }
    }
  }
}