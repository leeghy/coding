#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
char A[4], B[4];
int C, D;
int main(void)
{
	scanf("%s %s", &A, &B);
	
	C = ((int)A[2] - 48) * 100 + ((int)A[1] - 48) * 10 + (int)A[0] - 48;
	D = ((int)B[2] - 48) * 100 + ((int)B[1] - 48) * 10 + (int)B[0] - 48;

	if (C > D)
	{
		printf("%d", C);
	}
	else
	{
		printf("%d", D);
	}
	return 0;
}