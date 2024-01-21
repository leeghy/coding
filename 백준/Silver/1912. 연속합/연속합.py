N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = lst[1]

for i in range(2, N + 1):
    dp[i] = max(lst[i], dp[i - 1] + lst[i])


mx = -1000
for i in range(1, N+1):
    if dp[i] > mx:
        mx = dp[i]

print(mx)