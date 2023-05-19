#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int N;
	scanf("%d", &N);

	int first = N;
	int N_array[2];
	if (N < 10)
	{
		N_array[0] = 0;
		N_array[1] = N;
	}
	else
	{
		N_array[0] = N / 10;
		N_array[1] = N % 10;
	}

	int new_array[2];
	int cnt = 0;

	int plus = N_array[0] + N_array[1];

	while (1)
	{
		if (plus < 10)
		{
			N_array[0] = N_array[1];
			N_array[1] = plus;
		}

		else
		{
			N_array[0] = N_array[1];
			N_array[1] = plus % 10;
		}
		plus = N_array[0] + N_array[1];

		cnt += 1;

		if (first == N_array[0] * 10 + N_array[1])
		{
			printf("%d", cnt);
			break;
		}

	}



	
	

	return 0;
}