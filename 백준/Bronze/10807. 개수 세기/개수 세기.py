n = int(input())
listn = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(n):
    if listn[i] == v:
        cnt += 1

print(cnt)