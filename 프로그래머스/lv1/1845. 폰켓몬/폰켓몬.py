def solution(nums):
    answer = 0
    lens = len(nums)
    nums = set(nums)
    if len(nums) == lens//2:
        answer = lens//2
    elif len(nums) > lens//2:
        answer = lens//2
    else:
        answer = len(nums)
    
    return answer