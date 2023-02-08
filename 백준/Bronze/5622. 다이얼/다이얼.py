word = input()
num = []
ans = 0
for i in word:
    if 65<=ord(i)<68:
        num.append(2)
    elif 68<=ord(i)<71:
        num.append(3)
    elif 71<=ord(i)<74:
        num.append(4)
    elif 74<=ord(i)<77:
        num.append(5)
    elif 77<=ord(i)<80:
        num.append(6)
    elif 80<=ord(i)<84:
        num.append(7)
    elif 84<=ord(i)<87:
        num.append(8)
    else:
        num.append(9)

for j in num:
    ans += j + 1

print(ans)