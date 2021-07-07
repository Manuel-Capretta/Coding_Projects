#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

//Var
int balance;
int pin;
char name[20];
char surname[20];

//Transaction struct
struct transaction {
  int amount;
  char reason[100];
};

//Func
void acc();

int main(void){
  acc();

  return 0;
}

void acc(){
  printf("------------ Bank Management System ------------\n");
}
