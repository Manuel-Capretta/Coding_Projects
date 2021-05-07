#include <stdio.h>

int main() {
  int a[] = {1,1,2,3,5,8,13,21,34,55,89};
  int b[] = {1,2,3,4,5,6,7,8,9,10,11,12,13};
  int i = 0;
  int j = 0;
  while (j < sizeof(b)) {
    int aNumber = a[i];
    if (a[i] == b[j]) {
      printf("%da %d", a[i], b[j]);
      i++;
    } else {
      j++;
    }
  }
}