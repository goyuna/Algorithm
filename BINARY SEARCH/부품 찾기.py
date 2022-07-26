'''
이것이 코딩테스트다
실전문제 7-1 부품 찾기
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
'''

'''
입력조건
 * 첫째 줄에 정수 N이 주어진다.(1<=N<=1,000,000)
 * 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
 * 셋째 줄에는 정수 M이 주어진다.(1<=M<=1,000,000)
 * 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
'''

'''
출력조건
 * 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
'''

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 정수 N 입력받기
n = int(input())
# N개의 부품 고유 번호 입력받기
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 위해 사전에 정렬 수행
# 정수 M 입력받기
m = int(input())
# M개의 부품 고유 번호 입력받기
x = list(map(int, input().split()))

# 손님이 요청한 부품 번호 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')