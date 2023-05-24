#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char s[101] = { 0 };
	scanf("%s", s);
	
	int alphabet[27] = { 0 };
	for (int i = 0; i < 27; i++)
	{
		alphabet[i] = -1;
	}
	
	for (int i = 0; s[i] != '\0'; i++)
	{
		if (alphabet[(int)s[i] - 97] == -1)
		{
			alphabet[(int)s[i] - 97] = i;
		}
		else
		{
			continue;
		}
		
	}
	for (int i = 0; i < 26; i++)
	{
		printf("%d ", alphabet[i]);
	}

}