n = int(input())
m = 1000 - n

coin_types = [500, 100, 50, 10, 5, 1]

cnt = 0

for coin in coin_types:
    if m<coin:
        continue
    cnt += m//coin
    m %= coin

print(cnt)
