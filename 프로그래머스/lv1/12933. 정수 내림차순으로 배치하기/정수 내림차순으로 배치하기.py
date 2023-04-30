def solution(n):
    answer = 0
    n = str(n)
    n = list(n)
    n = sorted(n)
    n = list(reversed(n))
    answer = "".join(n)
    answer = int(answer)
    
    return answer