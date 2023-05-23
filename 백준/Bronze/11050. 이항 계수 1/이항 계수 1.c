#include <stdio.h>

typedef struct number {
	int x, y;
}NUM;

int cal(NUM* pt1)
{
	int sum = 1;
	int a = pt1->x;

	for (int i = 0; i < pt1->y; i++)
	{
		sum *= a;
		a--;
	}
	for (int i = 1; i <= pt1->y; i++)
	{
		sum /= i;
	}
	return sum;

}

int main(void)
{
	NUM p1;
	scanf("%d %d", &p1.x, &p1.y);
	printf("%d", cal(&p1));
	return 0;
}