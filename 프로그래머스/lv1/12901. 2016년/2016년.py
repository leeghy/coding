from datetime import date
def solution(a, b):
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    a = date(2016, a, b)
    a = a.weekday()
    answer = day[a]
    return answer