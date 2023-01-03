nums = list(map(int, input().split(' ')))

for i in range(len(nums)):
    nums[i] = int(str(nums[i])[::-1])

print(max(nums))