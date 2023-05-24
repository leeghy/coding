#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char str[1000001];
	scanf("%[^\n]s", str);
	getchar();
	int cnt = 0;
	int len = strlen(str);
	if (str[0] == ' ')
	{
		cnt -= 1;
	}
	if (str[len - 1] == ' ')
	{
		cnt -= 1;
	}
	for (int i = 0; str[i] != '\0'; i++)
	{
		if (str[i] == ' ')
		{
			cnt++;
		}
	}
	printf("%d", cnt+1);
}