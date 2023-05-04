def solution(n, arr1, arr2):
    answer = []
    two_1 = []
    two_2 = []
    for i in range(n):
        b = format(arr1[i], 'b')
        c = format(arr2[i], 'b')
        
        two_1.append(b)
        two_2.append(c)
        
    for i in range(n):
        s = ""
        if len(two_1[i]) < n:
            a = two_1[i]
            two_1[i] = '0'*(n-len(two_1[i])) + a
        if len(two_2[i]) < n:
            a = two_2[i]
            two_2[i] = '0'*(n-len(two_2[i])) + a
        for j in range(n):
            if int(two_1[i][j]) + int(two_2[i][j]) >= 1:
                s += '#'
            else:
                s += ' '
        answer.append(s)
            
        
    
    
            
        
    
    return answer