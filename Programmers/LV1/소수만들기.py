# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    result = 0

    li = list(combinations(nums, 3))    # 조합 구하기
    for i in range(len(li)):
        n = sum(li[i])
        # 소수인지 확인
        m = 0
        for i in range(2, n):
            if n%i == 0:
                m = 1
        if m == 0:
            result += 1

    return result

nums = [1,2,7,6,4]
print(solution(nums))

# 다른 사람 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):    # for-else문 사용
            if cand%j==0:
                break
        else:
            answer += 1
    return answer