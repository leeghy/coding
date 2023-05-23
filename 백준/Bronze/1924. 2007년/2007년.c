#include <stdio.h>

typedef struct Day {
	int x, y;
}DAY;

int cal(DAY* p1, int* date)
{
	int n = 0;
	for (int i = 0; i < p1->x; i++)
	{
		n += date[i];
	}
	n += p1->y;

	return n % 7;
}

int main(void)
{
	DAY p1;
	int date[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	scanf("%d %d", &p1.x, &p1.y);

	char* ans[8] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
	int n = cal(&p1, date);

	printf("%s", *(ans + n));
}