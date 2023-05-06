def solution(s):
    answer = 0
    num_dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_li = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while True:
        try:
            s = int(s)
            break
        except Exception:
            for i in num_li:
                if i in s:
                    s = s.replace(i, str(num_dic[i]))
        
    answer = s
    return answer