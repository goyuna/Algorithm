# 다이나믹 프로그래밍
n = int(input())
schedule = [list(map(int, input().split())) for i in range(n)]

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for i in range(n+1)]

# 다이나믹 프로그래밍 진행(bottom-up)
for i in range(n):
    for j in range(i + schedule[i][0], n+1):
        if d[j] < d[i] + schedule[i][1]:
            d[j] = d[i] + schedule[i][1]

print(d[-1])