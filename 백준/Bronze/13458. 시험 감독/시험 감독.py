n = int(input())
a = input()
anum = list(map(int, a.split()))
b, c = map(int, input().split())
ans = 0

for i in anum:
    if i-b <= 0:
        continue
    elif (i - b) % c == 0:
        num = (i - b) // c
    else:
        num = (i - b) // c + 1
    ans += num
ans += n
print(ans)