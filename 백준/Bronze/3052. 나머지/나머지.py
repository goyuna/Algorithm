divList = []

for _ in range(10):
    n = int(input())
    divList.append(n%42)
    
divSet = set(divList)
print(len(divSet))