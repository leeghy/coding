def solution(my_string, overwrite_string, s):
    
    answer_li = list(my_string)
        
    j = 0
    for i in range(s, len(overwrite_string)+s):
        answer_li[i] = overwrite_string[j]
        j += 1
    
    answer = "".join(answer_li)
    return answer