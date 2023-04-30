def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] not in score.keys():
                continue
            else:
                sum += int(score[photo[i][j]])
            
        answer.append(sum)
    return answer