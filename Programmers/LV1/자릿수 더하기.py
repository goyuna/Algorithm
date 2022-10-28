#https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    n = list(map(int, str(n)))  #int n을 str로 형변환하고 리스트로 변환
    return sum(n)

print(solution(987))