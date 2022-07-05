#이것이 코딩테스트다
#실전문제2. 큰 수의 법칙
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
array = list(map(int, input().split()))

array.sort()
first = array[n-1]  #가장 큰 수
second = array[n-2] #두 번째로 큰 수

count = int(m / (k + 1) * k)
count += m% (k + 1)

sum = 0
sum += (count) * first #가장 큰 수 더하기
sum += (m - count) * second # 두 번쩨로 큰 수 더하기 
print(sum)
