#include <stdio.h>
int main() {
	int x, b = 0, c, a;
	printf("Input a number: ");
	scanf("%d", &x);
	printf("\n");
		a = x;
    while (x != 0) { //reverse integer algorythm
        c = x % 10;
        b = b * 10 + c;
        x /= 10;
    }
		printf("%d / %d\n",a,b);
		if(a >= 0){
			if(a == b){
				printf("true\n");
			} else {
				printf("false\n");
			}
		} else {
			printf("false\n");
		}
}
