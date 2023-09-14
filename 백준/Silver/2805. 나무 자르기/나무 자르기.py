N, M = map(int, input().split())

height = list(map(int, input().split()))

start = 1
end = max(height)

while start <= end:
    ans = []
    mid = (start + end) // 2

    for i in height:
        if i - mid > 0:
            ans.append(i - mid)
        else:
            continue

    summation = sum(ans)
    if summation >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
