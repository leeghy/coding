#include <stdio.h>
#include <stdlib.h>

typedef struct str {
	char word[101];

}STR;

void cut(STR* pt1)
{
	int len = strlen(pt1->word);
	int j = 0;
	for (int i = 0; i < len; i++)
	{
		printf("%c", *(pt1->word + i));
		j++;
		if (j == 10)
		{
			printf("\n");
			j = 0;
		}
	}
}

int main(void)
{
	STR p1;
	scanf("%s", &p1.word);
	getchar();

	cut(&p1);
}