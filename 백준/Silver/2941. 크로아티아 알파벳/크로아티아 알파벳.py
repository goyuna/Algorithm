word = input()
c_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c_alp:
    word = word.replace(i, '*')
print(len(word))