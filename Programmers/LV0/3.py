'''
자릿수 더하기

문제 설명
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

제한사항
0 ≤ n ≤ 1,000,000
'''

def solution(n):
    answer = 0
    n = list(map(int,str(n)))
    
    for i in n:
        answer += i
    return answer

'''
!정수 배열로 변환!
num = 12345
strnum = list(map(int,str(n)))
 -> strnum = [1,2,3,4,5]
'''
