def solution(n):
    answer = 0
    n = list(map(int,str(n)))
    
    for i in n:
        answer += i
    return answer