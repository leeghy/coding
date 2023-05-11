def solution(a, b, n):
    answer = 0
    
    while True:
        if n < a:
            break
        num = n // a #20//3=6, 6*3
        answer += num*b
        n = n - (num*a) + (num*b)
        
    return answer