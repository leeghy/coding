def even(n):
    return n / 2
def odd(n):
    return 3 * n + 1

def solution(num):
    answer = 0
    while (num != 1):  
        if answer >= 500:
            answer = -1
            break
        if num % 2 == 0:
            num = even(num)
            answer += 1
        else:
            num = odd(num)
            answer += 1
        
        
    return answer