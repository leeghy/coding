#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int max = 0;
	int line = 0;
	int board[9][9] = { 0, };

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			scanf("%d", &board[i][j]);
			if (board[i][j]>max)
			{
				max = board[i][j];
				line = 10 * i + j;
			}
		}
	}
	printf("%d\n", max);
	printf("%d %d", line / 10 + 1, line % 10 +1);
	return 0;
}