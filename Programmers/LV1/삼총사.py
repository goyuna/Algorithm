#https://school.programmers.co.kr/learn/courses/30/lessons/131705
'''
세가지 수로 만들 수 있는 모든 케이스를 combinations으로 만들고,
그 케이스 중 모든 수의 합이 0일 경우만 남겨 리스트의 길이를 반환
'''

def solution(number):
    answer = 0

    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer

print(solution([-2,3,0,2,-5]))