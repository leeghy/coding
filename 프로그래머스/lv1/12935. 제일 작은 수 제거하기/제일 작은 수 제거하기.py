def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = arr
    if answer == []:
        answer = [-1]
    return answer