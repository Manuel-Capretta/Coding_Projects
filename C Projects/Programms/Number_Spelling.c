#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int main(void){
  int num;
  
  char* nums[10] = {"null","eins","zwei","drei","vier","fünf","sechs","sieben","acht","neun"};

  scanf("%d", &num);

  switch (num){
  case 0:
    printf("%s", nums[0]);
    break;
  case 1:
    printf("%s", nums[1]);
    break;
  case 2:
    printf("%s", nums[2]);
    break;
  case 3:
    printf("%s", nums[3]);
    break;
  case 4:
    printf("%s", nums[4]);
    break;
  case 5:
    printf("%s", nums[5]);
    break;
  case 6:
    printf("%s", nums[6]);
    break;
  case 7:
    printf("%s", nums[7]);
    break;
  case 8:
    printf("%s", nums[8]);
    break;
  case 9:
    printf("%s", nums[9]);
    break;
  default:
    break;
  }


  return 0;
}