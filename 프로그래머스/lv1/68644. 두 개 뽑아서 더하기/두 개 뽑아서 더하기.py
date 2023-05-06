def solution(numbers):
    answer = []
    numbers = sorted(numbers)
    li = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            li.append(numbers[i] + numbers[j])
    li = list(set(li))
    answer=sorted(li)
    return answer