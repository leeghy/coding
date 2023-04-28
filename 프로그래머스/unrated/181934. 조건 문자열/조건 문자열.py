def solution(ineq, eq, n, m):
    answer = 0
    
    if eq == '!':
        if ineq == '<':
            if n < m:
                answer = 1
            else:
                answer = 0
        else:
            if n > m:
                answer = 1
            else:
                answer = 0
            
    else:
        if ineq == '<':
            if n <= m:
                answer = 1
            else:
                answer = 0
        else:
            if n >= m:
                answer = 1
            else:
                answer = 0
                
                
    return answer