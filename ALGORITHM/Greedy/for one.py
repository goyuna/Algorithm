'''
이것이 코딩테스트다
실전문제 3-4 1이 될 때까지
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
 1. N에서 1을 뺀다.
 2. N을 K로 나눈다. 
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.
'''

'''
입력조건
 * 첫째 줄에 N(2<=N<=100,000)과 K(2<=K<=100,000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
출력조건
 * 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 획수의 최솟값을 출력한다.
'''

# 아이디어 : n을 k로 나눌 수 있으면 나누기, 나눌 수 없으면 나눌 수 있을 때까지 1을 빼기

N, K = map(int, input().split())

cnt = 0

# N이 K 이상이라면 K로 계속 나누기
while N >= K:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while N % K != 0:
        N -= 1
        cnt += 1
    # K로 나누기
    N //= K
    cnt += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while N > 1:
    N -= 1
    cnt += 1

print(cnt)

#더 효율적 방법 다시 공부 필요