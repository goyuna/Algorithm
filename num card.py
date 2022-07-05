#이것이 코딩테스트다
#실전문제4. 1이 될 때까지

n, m = map(int, input().split())
i = 0

while True:
    #(N == M로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // m) * m
    i += (n - target)
    n = target
    #N이 M보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < m:
        break
    #m로 나누기
    i += 1
    n //= m

#마지막으로 남은 수에 대하여 1씩 빼기
i += (n - 1)
print(i)