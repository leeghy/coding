#include <stdio.h>
#include <stdlib.h>

int compare(const void* first, const void* second)
{
	if (*(int*)first > *(int*)second)
	{
		return 1;
	}
	else if (*(int*)first < *(int*)second)
	{
		return -1;
	}
	else
	{
		return 0;
	}

}
int main(void)
{
	int N;
	scanf("%d", &N);

	int* num = (int*)malloc(sizeof(int) * N);

	
	for (int i = 0; i < N; i++)
	{
		scanf("%d", num + i);
	}
	
	qsort(num, (size_t*)N, sizeof(num[0]), compare);

	
	for (int i = 0; i < N; i++)
	{
		printf("%d\n", *(num + i));
	}
	
}