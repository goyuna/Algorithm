#https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    lens = len(set(nums))
    
    if lens > (len(nums)//2):
        answer = len(nums)//2
    else:
        answer = lens
    return answer

print(solution([3,3,3,2,2,2]))