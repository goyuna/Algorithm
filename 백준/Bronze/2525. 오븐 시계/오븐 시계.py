a, b = map(int, input().split())
c = int(input())

nb = b+c
if nb >= 60:
    nb %= 60
    a += ((b+c)//60)
    if a>23:
        a -= 24

print(a, nb)