def solution(s, n):
    answer = ''
    li_s = list(s)
    for i in li_s:
        if i == ' ':
            answer += ' '
        else:
            if (ord(i) + n > 90 and 65 <= ord(i) and ord(i) <= 90) or (ord(i) + n > 122 and 97 <= ord(i) and ord(i) <= 122):
                answer += chr(ord(i) - 26 + n)
            else:
                answer += chr(ord(i) + n)
    return answer