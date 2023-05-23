#include <stdio.h>

typedef struct number {
	int x[9];
}NUM;

void ans(NUM* p1, char answer[])
{
	int asc = 0;
	int dec = 0;
	for (int i = 1; i < 8; i++)
	{
		if (p1->x[i] == p1->x[i-1] + 1)
		{
			asc++;
		}
		else if (p1->x[i] == p1->x[i-1] - 1)
		{
			dec++;
		}
		else
		{
			asc = 0, dec = 0;
			strcpy(answer, "mixed");
			return;
		}
	}
	if (asc == 7)
	{
		strcpy(answer, "ascending");
		return;
	}
	else if (dec == 7)
	{
		strcpy(answer, "descending");
		return;
	}
}

int main(void)
{
	NUM p1;
	for (int i = 0; i < 8; i++)
	{
		scanf("%d", &p1.x[i]);
	}
	char answer[12];
	ans(&p1, answer);
	
	printf("%s", answer);
	return 0;
}