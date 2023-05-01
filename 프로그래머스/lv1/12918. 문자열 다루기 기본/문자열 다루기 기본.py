def solution(s):
    answer = True
    
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            try:
                nu = int(s[i])
            except Exception:
                answer = False
        
    
    else:
        answer = False            
    return answer