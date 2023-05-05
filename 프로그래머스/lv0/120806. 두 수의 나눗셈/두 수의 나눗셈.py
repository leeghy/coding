def solution(num1, num2):
    answer = 0
    answer = num1 / num2 * 1000
    n = str(answer)
    a = ""
    for i in n:
        if i == '.':
            break
        else:
            a += i
    answer = int(a)
    return answer