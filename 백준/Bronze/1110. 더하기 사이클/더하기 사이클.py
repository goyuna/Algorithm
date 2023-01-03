n = int(input())
cnt = 0
a , b = divmod(n, 10)

while True:
    plus = a+b
    new_num = (b*10) + (plus%10)
    cnt += 1
    if new_num == n:
        break
    else:
        a, b = divmod(new_num, 10)
        continue

print(cnt)