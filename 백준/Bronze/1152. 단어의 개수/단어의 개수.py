s = input().strip()
s = s.split(' ')

for i in s:
    if i == '':
        s.remove(i)
print(len(s))