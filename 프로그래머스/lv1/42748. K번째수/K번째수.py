def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        li = []
        a = commands[i][0]
        b = commands[i][1]
        for j in range(a-1, b):
            li.append(array[j])
        li = sorted(li)
        
        answer.append(li[commands[i][2]-1])
    return answer