N, K = map(int, input().split())

st1 = [i for i in range(1, N + 1)]

ans = []
num = 0

for i in range(N):
    num += K-1
    if num >= len(st1):
        num %= len(st1)

    ans.append(str(st1.pop(num)))

print("<" + ", ".join(ans) + ">")