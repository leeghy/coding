def solution(d, budget):
    answer = 0
    d = sorted(d)
    if sum(d) <= budget:
        answer = len(d)
    else:
        while True:
            d.remove(max(d))
            if sum(d) <= budget:
                answer = len(d)
                break
            
            
    return answer