def sol(n):
    ans = 0
    if n < 100:
        ans = n
    else:
        ans += 99
        for i in range(100, n+1):
            num = str(i)
            if (int(num[1])-int(num[0])) == (int(num[2])-int(num[1])):
                ans +=1

    return ans

n = int(input())
print(sol(n))