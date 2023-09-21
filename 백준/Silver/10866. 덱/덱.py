import sys
from collections import deque

d = deque()
N = int(sys.stdin.readline())

for i in range(N):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push_front':
        d.appendleft(order[1])
    elif order[0] == 'push_back':
        d.append(order[1])
    elif order[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            x = d.popleft()
            print(x)
    elif order[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            x = d.pop()
            print(x)
    elif order[0] == 'size':
        print(len(d))
    elif order[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    else:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])