#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

struct st {
  int a;
  char c[20];
};

char test[50];


int main() {
  struct st st_arr[3]; // Declare an array of 3 structure objects 

  struct st st_obj0; // first structure object
  st_obj0.a = 1;
  fgets(test, 50, stdin);
  strncpy(st_obj0.c, test, 20);

  struct st st_obj1; //Second structure object
  st_obj1.a = 2;
  strncpy(st_obj1.c, "Pedda", 20);

  struct st st_obj2; // Third structure object
  st_obj2.a = 4;
  strncpy(st_obj2.c, "Dan ooo", 20);

  st_arr[0] = st_obj0; // Initializing first element of array with first structure object
  st_arr[1] = st_obj1; // Initializing second element of array with second structure object
  st_arr[2] = st_obj2; // Initializing third element of array with third structure object 

  printf("\n First Element of array has values of a = [%d] and c = [%s]\n", st_arr[0].a, st_arr[0].c);
  printf("\n Second Element of array has values of a = [%d] and c = [%s]\n", st_arr[1].a, st_arr[1].c);
  printf("\n Third Element of array has values of a = [%d] and c = [%s]\n", st_arr[2].a, st_arr[2].c);

  return 0;
}