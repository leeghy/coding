def solution(arr):
    answer = []
    arr.append(-1)
    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
            
    return answer