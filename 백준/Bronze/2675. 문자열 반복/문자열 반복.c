#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
char S[1001];
int main(void)
{
	int T = 0, n=0;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		scanf("%d", &n);
		scanf("%s", S);
		for (int j = 0; S[j] != '\0'; j++)
		{
			for (int k = 0; k < n; k++)
			{
				printf("%c", S[j]);
			}
		}
		printf("\n");
	}
	
	return 0;
}


