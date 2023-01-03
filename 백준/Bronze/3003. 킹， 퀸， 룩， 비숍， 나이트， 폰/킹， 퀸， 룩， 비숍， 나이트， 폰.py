chess = [1,1,2,2,2,8]
comp = list(map(int, input().split()))
answer = []

for i in range(len(chess)):
    answer.append(chess[i]-comp[i])

for j in answer:
    print(j, end=" ")