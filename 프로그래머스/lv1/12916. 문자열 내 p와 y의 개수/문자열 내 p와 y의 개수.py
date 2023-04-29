def solution(s):
    answer = True
    p_nu = 0
    y_nu = 0
    for i in s:
        if i == 'P' or i == 'p':
            p_nu += 1
        if i == 'Y' or i == 'y':
            y_nu += 1
    
    
    if p_nu == y_nu:
        answer = True
    else:
        answer = False

    return answer