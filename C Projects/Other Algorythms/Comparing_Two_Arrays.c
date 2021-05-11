#include <stdio.h>

int main(){
  int a[] = {1,1,2,3,5,8,13,21,34,55,89};
  int b[] = {1,2,3,4,5,6,7,8,9,10,11,12,13};
  int countA = 0;
  int countB = 0;
  while (countA < sizeof(a)){
    if(a[countA] == b[countB]){
      printf("%d %d", a[countA], b[countB]);
      countA++;
    } else {
      countB++;
    }
  }
}