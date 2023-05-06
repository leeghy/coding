def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    li = list(reversed(answer))
    ans_rev = "".join(li)
    answer = answer + '0' + ans_rev
    print(answer)
    return answer