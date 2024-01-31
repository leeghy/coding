n = int(input())

data = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

dp[1] = 1

for i in range(2, n + 1):
    mx = 0
    idx = 0
    for j in range(1, i):
        if data[i] < data[j] and dp[j] > mx:
            mx = dp[j]
            idx = j

    if mx == 0:
        dp[i] = 1
    else:
        dp[i] = dp[idx]+1

print(max(dp))