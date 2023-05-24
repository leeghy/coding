#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void)
{
	int T = 0;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		char word[1001] = { 0 };
		scanf("%s", word);
		printf("%c", word[0]);
		printf("%c", word[strlen(word)-1]);
		printf("\n");
	}
}