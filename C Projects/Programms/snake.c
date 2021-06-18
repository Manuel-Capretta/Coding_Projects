#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int input(int direction);

int direction;

int main(void){
  input(direction);

  switch(direction){
  case 1:
    printf("Up");
    break;
  case 2:
    printf("left");
    break;
  case 3:
    printf("Down");
    break;
  case 4:
    printf("right");
    break;
  }
}

int input(int direction){
  char user_input[] = {};
  printf("User Input: \n");
  fgets(user_input, 20, stdin); //get input

  /*if(user_input == 'w'){
    direction = 1;
  }else if(user_input == 'a'){
    direction = 2;
  }else if(user_input == 's'){
    direction = 3;
  }else if(user_input == 'd'){
    direction = 4;
  }*/
  direction = 1;

  return direction;
}