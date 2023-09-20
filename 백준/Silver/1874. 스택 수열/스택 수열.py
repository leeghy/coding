n = int(input())

stack = []
sequence = []
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        sequence.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        sequence.append('-')
    else:
        print("NO")
        break

else:
    for j in sequence:
        print(j)