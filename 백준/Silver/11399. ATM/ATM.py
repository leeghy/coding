N = int(input())
li = list(map(int, input().split()))
li = sorted(li)
sum = 0
n = 0
for i in li:
    n += i
    sum += n
print(sum)