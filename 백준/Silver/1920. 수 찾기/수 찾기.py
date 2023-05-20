import sys
N = int(input())
li_N = list(map(int, sys.stdin.readline().split()))
M = int(input())
li_M = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid+1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

li_N.sort()

for i in li_M:
    if binary_search(li_N, i, 0, N-1) == None:
        print(0)
    elif binary_search(li_N, i, 0, N-1) != None:
        print(1)