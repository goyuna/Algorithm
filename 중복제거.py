n = int(input())
array = list(map(int, input().split()))

# 각 원소 하나씩 확인
for i in range(n):
  target = array[i]
  for j in array[i+1:]:
    if j == target:
      n -= 1

print(n)