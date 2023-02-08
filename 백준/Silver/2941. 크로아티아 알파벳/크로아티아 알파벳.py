word = input()
c_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0

for i in range(len(word)):
    if word[0:2] in c_alp:
        ans += 1
        word = word[2:]
    elif word[0:3] in c_alp:
        ans += 1
        word = word[3:]
    elif word == '':
        break
    else:
        ans += 1
        word = word[1:]

print(ans)