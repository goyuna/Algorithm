# https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 에라토스테네스의 체 이용
def prime_list(n):
    answer = 0

    # n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
    m = int((n+1) ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:            #i가 소수인 경우
            for j in range(i+i, n+1, i):  #i이후 i의 배수들을 False판정
                sieve[j] = False
    
    # 소수 개수 산출
    for i in range(2, n+1):
        if sieve[i] == True:
            answer += 1

    # 소수 목록 산출
    return answer


#다른 사람 풀이
def solution(n):
    num = set(range(2, n+1))    # set : 중복허용하지 않음, 순서가 없음

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))

    return len(num)

n = 1000000
print(prime_list(n))