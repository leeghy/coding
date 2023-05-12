cnt = []
def merge(x):
    global cnt
    if len(x) == 1:
        return x
    else:
        mid = (len(x)+1) // 2
        left = merge(x[:mid])
        right = merge(x[mid:])

        sort_li = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sort_li.append(left[i])
                cnt.append(left[i])
                i += 1
            else:
                sort_li.append(right[j])
                cnt.append(right[j])
                j += 1
        
        while i < len(left):
            sort_li.append(left[i])
            cnt.append(left[i])
            i += 1
        while j < len(right):
            sort_li.append(right[j])
            cnt.append(right[j])
            j += 1
    
    return sort_li

N, k = map(int,input().split())
a = list(map(int, input().split()))

merge(a)
if len(cnt) < k:
    print(-1)
else:
    print(cnt[k-1])