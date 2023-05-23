#include <stdio.h>

typedef struct number {
	int x[6];
}NUM;

void check(NUM* pt1, int* ans)
{
	int sum = 0;
	for (int i = 0; i < 5; i++)
	{
		sum += (pt1->x[i]) * (pt1->x[i]);
	}
	*ans = sum % 10;
}

int main(void)
{
	NUM p1;
	for (int i = 0; i < 5; i++)
	{
		scanf("%d", &p1.x[i]);
		getchar();
	}
	int answer = 0;
	check(&p1, &answer);
	printf("%d", answer);
}