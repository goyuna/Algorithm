#이것이 코딩 테스트다
#예제 4-2. 시각

t = int(input())

count = 0
for i in range(t + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)