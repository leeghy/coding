def solution(t, p):
    answer = 0
    n = len(p)
    nu = []
    for i in range(len(t)):
        s = ""
        s += t[i]
        if i+n > len(t):
            break
        for j in range(i+1, i+n):
            s += t[j]
        nu.append(s)
    for i in nu:
        if int(i) <= int(p):
            answer += 1
    return answer