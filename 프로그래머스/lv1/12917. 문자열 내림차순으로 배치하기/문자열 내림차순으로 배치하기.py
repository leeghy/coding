def solution(s):
    answer = ''
    s = sorted(s)
    s = list(reversed(s))
    answer = "".join(s)
    return answer