#https://school.programmers.co.kr/learn/courses/30/lessons/42586
#스택/큐

def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        if ((100 - progresses[i])% speeds[i]) ==0:
            days.append((100 - progresses[i])// speeds[i])
        else:
            days.append(((100 - progresses[i])// speeds[i]) + 1)

    

    return answer