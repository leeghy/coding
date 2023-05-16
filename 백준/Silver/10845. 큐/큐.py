from collections import deque

queue = deque()
order= []
N = int(input())
for i in range(N):
    order.append(input())

for i in order:
    if 'push' in i:
        a = i.replace('push', '')
        queue.append(int(a))
    elif i == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif i == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif i == 'size':
        print(len(queue))
    elif i == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif i == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            v = queue.popleft()
            print(v)