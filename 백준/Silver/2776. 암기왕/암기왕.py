import sys


def binary_search(start, end, arr, target):
    if start > end:
        return '0'

    mid = (start + end) // 2
    if arr[mid] == target:
        return '1'
    elif arr[mid] > target:
        return binary_search(start, mid - 1, arr, target)
    else:
        return binary_search(mid + 1, end, arr, target)


T = int(input())

for k in range(T):
    N = int(input())
    data = list(map(int, sys.stdin.readline().split()))
    sorted_data = sorted(data)

    M = int(input())
    target = list(map(int, sys.stdin.readline().split()))
    
    for i in range(M):
        print(binary_search(0, N-1, sorted_data, target[i]))
