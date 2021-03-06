'''
이것이 코딩테스트다 
예제 3-1 거스름돈
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 떄 거슬러줘여 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야할 돈 N은 항상 10의 배수이다.
'''

N = int(input())

count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += N // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    # // : 나누기 연산 후 소수점 이하 수 버림
    N %= coin

print(count)

'''
화폐의 종류만큼 반복을 수행하므로 화폐의 종류가 K개라고 할 때 소스코드의 시작복잡도는 O(K)
'''