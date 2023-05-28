#include <stdio.h>

int main(void)
{
	int A, B;
	scanf("%d %d", &A, &B);

	int arr1[101][101];
	int arr2[101][101];

	int(*p1)[101] = arr1;
	int(*p2)[101] = arr2;
	for (int i = 0; i < A; i++)
	{
		for (int j = 0; j < B; j++)
		{
			scanf("%d", *(p1 + i) + j);
		}
	}
	for (int i = 0; i < A; i++)
	{
		for (int j = 0; j < B; j++)
		{
			scanf("%d", *(p2 + i) + j);
		}
	}
	/*printf("------------\n");
	for (int i = 0; i < A; i++)
	{
		for (int j = 0; j < B; j++)
		{
			printf("%d ", *(*(p1 + i) + j));
		}
		printf("\n");
	}
	for (int i = 0; i < A; i++)
	{
		for (int j = 0; j < B; j++)
		{
			printf("%d ", *(*(p2 + i) + j));
		}
		printf("\n");
	}
	printf("----------------------\n");*/
	for (int i = 0; i < A; i++)
	{
		for (int j = 0; j < B; j++)
		{
			printf("%d ", *(*(p1 + i) + j) + *(*(p2 + i) + j));
		}
		printf("\n");
	}

}