def solution(x):
    answer = True
    nu = 0
    for i in range(len(str(x))):
        nu += int(str(x)[i])
    if x % nu == 0:
        answer = True
    else:
        answer = False
    return answer