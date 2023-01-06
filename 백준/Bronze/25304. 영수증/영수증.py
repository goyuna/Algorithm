x = int(input())    # 총금액
n = int(input())    # 물건 종류의 수
sum = 0

for i in range(n):
    a,b=map(int,input().split())    # 각 물건 가격과 개수
    sum += a*b

if(x==sum):print("Yes")
else: print("No")