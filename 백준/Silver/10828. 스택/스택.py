import sys
N = int(sys.stdin.readline())

def top(li):
    if len(li) == 0:
        return -1
    else:
        return li[0]

def size(li):
    return len(li)

def pop(li):
    if len(li) == 0:
        return -1
    else:
        temp = li[0]
        temp2 = li.pop(temp)
        return temp2

def empty(li):
    if len(li) == 0:
        return 1
    else:
        return 0

stack = []
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        stack.insert(0, int(order[1]))
    elif order[0] == "top":
        print(top(stack))
    elif order[0] == "size":
        print(size(stack))
    elif order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            res = stack.pop(0)
            print(res)
    elif order[0] == "empty":
        print(empty(stack))