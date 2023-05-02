def division(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer
def solution(n, m):
    answer = []
    set1 = set(division(n))
    set2 = set(division(m))
    li = list(set1 & set2)
    answer.append(max(li))
    answer.append(n * m / max(li))
    return answer