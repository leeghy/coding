def solution(phone_number):
    answer = ''
    phone_li = list(phone_number)
    for i in range(0, len(phone_li)-4):
        phone_li[i] = '*'
    answer = "".join(phone_li)
    return answer