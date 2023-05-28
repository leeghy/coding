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
		return 1;
	}
}
int average(int* arr)
{
	int sum = 0;
	for (int i = 0; i < 5; i++)
	{
		sum += *(arr + i);
	}
	return sum / 5;
}

int main(void)
{
	int num[5] = { 0 };
	
	for (int i = 0; i < 5; i++)
	{
		scanf("%d", num + i);
	}

	qsort(num, (size_t*)5, sizeof(int), compare);
	printf("%d\n%d", average(&num), *(num + 2));
}