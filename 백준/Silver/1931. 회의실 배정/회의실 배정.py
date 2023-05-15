N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, input().split())))
a = []
num = 0
li = sorted(li, key=lambda x : (x[1], x[0]))

cnt = 1
n = li[0][1]
i=0
while True:
    i += 1
    if n <= li[i][0]:
        cnt += 1
        n = li[i][1]
    if i+1 == len(li):
        break
        
print(cnt)