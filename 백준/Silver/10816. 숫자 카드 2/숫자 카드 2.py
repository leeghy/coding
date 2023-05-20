import sys
N = int(input())
li_N = list(map(int, sys.stdin.readline().split()))
M = int(input())
li_M = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return dic[target]
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

dic = {}
li_N.sort()

for i in li_N:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

for i in li_M:
    ans = binary_search(li_N, i, 0, N-1)
    print(ans, end=' ')