import sys


def binary_search(target, data, start, end):
    if start > end:
        return '0'
    mid = (start + end) // 2

    if data[mid] == target:
        return '1'
    elif data[mid] > target:
        return binary_search(target, data, start, mid - 1)
    else:
        return binary_search(target, data, mid + 1, end)


N = int(input())
card = list(map(int, sys.stdin.readline().split()))
card.sort()
M = int(input())
check_card = list(map(int, sys.stdin.readline().split()))
size = len(card) - 1

for i in range(M):
    check_card[i] = binary_search(check_card[i], card, 0, N-1)

a =" ".join(check_card)

print(a)
