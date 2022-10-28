#https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0

    for i in range(a-1):
        day += month[i]
    
    day += b-1
    day %= 7
    answer = weeks[day]
    return answer

print(solution(2,10))

#-------------다른 사람 코드
def solution(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]