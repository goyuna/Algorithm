T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    f0 = [x for x in range(1, n+1)]   # 0층 리스트

    for i in range(k):  # 층 수만큼 반복
        for j in range(1, n):   # 1 ~ n-1까지
            f0[j] += f0[j-1]
    
    print(f0[-1])   # 가장 마지막 수 출력