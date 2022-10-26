#https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    rec = 0 # 받는 콜라 수

    while n>=a:
        rec = (n//a) * b
        n = n%a + rec
        answer += rec

    return answer
