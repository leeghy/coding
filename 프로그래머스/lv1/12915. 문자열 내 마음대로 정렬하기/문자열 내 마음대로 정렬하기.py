def solution(strings, n):
    answer = []
    dic = {}
    
    for i in range(len(strings)):
        dic[strings[i]] = strings[i][n]
    
    dic1 = sorted(dic.items(), key=lambda x:x[0])
    
    dic2 = sorted(dic1, key = lambda x:x[1])
    for i in range(len(dic2)):
        answer.append(dic2[i][0])
    return answer