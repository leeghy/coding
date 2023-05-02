def solution(n):
    answer = 0
    three = []
    while True:
        if n < 3:
            three.append(n)
            break
        three.append(n % 3)
        n = n // 3
        
    j = len(three)-1
    for i in range(len(three)):
        answer += three[i] * (3**j)
        j -= 1
    return answer