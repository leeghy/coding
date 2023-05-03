def solution(number):
    answer = 0
    li = []
    
    for i in range(len(number)):
        m = i+1
        for j in range(m, len(number)):
            for k in range(m+1, len(number)):
                li.append([number[i], number[j], number[k]])
            m+=1
    
    for i in li:
        if sum(i) == 0:
            answer += 1
    return answer