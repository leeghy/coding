T = int(input())

for i in range(T):
    sentence = list(input().split())
    tmp = ''
    for j in sentence:
        tmpli = list(reversed(j))
        for k in tmpli:
            tmp += k
        tmp += ' '
    print(tmp)