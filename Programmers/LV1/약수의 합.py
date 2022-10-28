#https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    sum = 0

    for i in range(1, n+1):
        if n % i ==0:
            sum += i
    
    return sum

print(solution(5))

# -------------다른 사람 풀이
def sumDivisior(num):
    return(sum([i for i in range(1, num+1) if num%i==0]))