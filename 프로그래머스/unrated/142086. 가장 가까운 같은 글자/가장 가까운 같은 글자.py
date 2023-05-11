def solution(s):
    answer = []
    li = ""
    for i in range(len(s)):
        if s[i] in li:
            a = li.rfind(s[i])
            
            answer.append(i-a)
            li += s[i]
            
        else:
            answer.append(-1)
            li+=(s[i])
        
    return answer