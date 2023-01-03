numbers = int(input())
nums_list = []

for i in range(numbers):
    nums_list.append(int(input()))

nums_list = sorted(nums_list)
for i in nums_list:
    print(i)