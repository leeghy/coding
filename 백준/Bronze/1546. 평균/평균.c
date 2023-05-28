#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int n;
float max = 0, score[1001];

int main(void)
{
	scanf("%d", &n);
	int input = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &input);
		score[i] = input;

		if (input > max)
		{
			max = input;
		}	
	}
	float sum = 0;

	for (int i = 0; i < n; i++)
	{
		sum += score[i] / max * 100;
	}
	
	printf("%lf", sum / n);

	return 0;
}