#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


int main(void)
{
	char word[101] = { 0 };
	scanf("%s", word);
	int i = 0, cnt = 0;
	while (1)
	{
		if (word[i] != '\0')
		{
			cnt++, i++;
		}
		else
		{
			printf("%d", cnt);
			break;
		}
	}
}