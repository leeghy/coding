import sys

K, N = map(int, sys.stdin.readline().split())

max = 0

data = []
for i in range(K):
    x = int(sys.stdin.readline())
    data.append(x)
    if x > max:
        max = x

start = 1
end = max

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in data:
        count += i // mid

    if count >= N:
        start = mid + 1

    else:
        end = mid - 1

print(end)
