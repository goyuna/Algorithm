# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = {}
    users = len(stages)    # 유저 수
    
    for i in range(1, N+1):
        cnt = stages.count(i)   # 클리어하지 못한 플레이어 수
        # 실패율 계산
        if users != 0: 
            answer[i] = cnt/users
            users -= cnt    # 다음 스테이지에 도달한 플레이어 수
        else : answer[i]=0

    return sorted(answer, key=lambda x: answer[x], reverse=True)

N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N, stages))