def solution(n):
    answer = []
    nu = len(str(n))
    for i in range(nu-1, -1, -1):
        answer.append(int((str(n)[i])))
    
    return answer