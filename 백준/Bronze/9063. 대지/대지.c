#include <stdio.h>

int main(void)
{
	int N = 0;
	scanf("%d", &N);
	int x[100001] = { 0, };
	int y[100001] = { 0, };
	for (int i = 0; i < N; i++)
	{
		scanf("%d %d", &x[i], &y[i]);
	}
	int x_Max = -10001, x_min = 10001;
	for (int i = 0; i < N; i++)
	{
		if (x[i] > x_Max)
		{
			x_Max = x[i];
		}
		if (x[i] < x_min)
		{
			x_min = x[i];
		}
	}
	int y_Max = -10001, y_min = 10001;
	for (int i = 0; i < N; i++)
	{
		if (y[i] > y_Max)
		{
			y_Max = y[i];
		}
		if (y[i] < y_min)
		{
			y_min = y[i];
		}
	}
	int size = (x_Max - x_min) * (y_Max - y_min);
	printf("%d", size);
}