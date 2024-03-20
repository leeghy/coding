def present_jisu(person, met):
    gift = sum(met[person])
    take = 0
    for i in range(len(met)):
        take += met[i][person]

        
        
    return gift - take


def solution(friends, gifts):
    answer = [0 for i in range(len(friends))]
    
    dic = {}
    for i in friends:
        for j in friends:
            s = i+' '+j
            dic[s]=0
    
    for i in gifts:
        dic[i] +=1
    
    metrix = []
    # for i in dic.keys():
        
    for i in friends:
        l = []
        for j in friends:
            s = i + ' ' + j
            l.append(dic[s])
        metrix.append(l)
            
        
#     print(dic)
#     print(metrix)
    
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            if i==j:
                continue
            else:
                if metrix[i][j] > metrix[j][i]:
                    answer[i] += 1
                    
                elif metrix[i][j] < metrix[j][i]:
                    answer[j] += 1
                else:
                    a = present_jisu(i, metrix)  #i의 선물지수
                    b = present_jisu(j, metrix) #j의선물지수
                    
                    if a>b:
                        answer[i] += 1
                    elif a<b:
                        answer[j] +=1
                    
                        
                    
    
    return max(answer)