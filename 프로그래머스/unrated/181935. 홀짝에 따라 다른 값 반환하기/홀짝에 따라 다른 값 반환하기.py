def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 2)
def two(n):
    ans = 0
    for i in range(2, n+1, 2):
        ans += i * i
    return ans

def solution(n):
    answer = 0
    
    if n % 2 == 0:
        answer = two(n)
    else:
        answer = sum(n)
    
    return answer