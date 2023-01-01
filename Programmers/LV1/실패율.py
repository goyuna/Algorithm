# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    users = len(stages)    # 유저 수
    
    for i in range(1, N+1):
        cnt = stages.count(i)   # 클리어하지 못한 플레이어 수
        # 실패율 계산
        if users == 0: fail  =0
        else : fail = cnt/users

        # 다음 스테이지에 도달한 플레이어 수 
        users -= cnt
        # 배열에 (스테이지 번호, 실패율) 추가
        answer.append((i, fail))
    
    # 실패율 내림차순을 기준으로 정렬
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    # 각 스테이지 번호를 실패율의 내림차순으로 정렬
    answer = [[i[0] for i in answer]]

    return answer

N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N, stages))