#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int set[10] = { 0, };
	
	char n[8] = { 0 };
	scanf("%s", n);
	int len = strlen(n);
	
	for (int i = 0; i < len; i++)
	{
		if (n[i] == '9' || n[i] == '6')
		{
			if (set[6] > set[9])
			{
				set[9]++;
			}
			else
			{
				set[6]++;
			}
		}
		else
		{
			for (int j = 0; j < 10; j++)
			{
				if (n[i] == (char)j + 48)
				{
					set[j]++;
					break;
				}
			}
		}
		
	}
	int max = 0;
	for (int i = 0; i < 10; i++)
	{
		if (set[i] > max)
		{
			max = set[i];
		}
	}
	printf("%d", max);
}