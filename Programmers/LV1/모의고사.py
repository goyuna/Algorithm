# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    result = []
    score = [0,0,0]

    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]

    # 정답 비교하여 점수 카운트
    for i, answer in enumerate(answers): # enumerate : 인덱스와 원소를 동시에 반복
        if answer == n1[i%len(n1)]:
            score[0] += 1
        if answer == n2[i%len(n2)]:
            score[1] += 1
        if answer == n3[i%len(n3)]:
            score[2] += 1
        
    # 최고득점자 찾기
    for i, answer in enumerate(score):
        if answer == max(score):
            result.append(i+1)
    
    return result

answers = [1,3,2,4,2]
print(solution(answers))