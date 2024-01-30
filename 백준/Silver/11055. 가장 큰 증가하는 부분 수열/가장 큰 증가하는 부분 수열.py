n = int(input())

data = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = data[1]

for i in range(2, n+1):
    mx = 0
    idx = 0
    for j in range(1, i):
        if dp[j] > mx and data[i] > data[j]:
            mx = dp[j]
            idx = j
    dp[i] = dp[idx] + data[i]

print(max(dp))