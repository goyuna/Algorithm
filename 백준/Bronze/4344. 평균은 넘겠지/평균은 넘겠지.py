c = int(input())    # 테스트케이스 개수

for _ in range(c):
    scores = list(map(int, input().split()))    # 학생 점수리스트
    avg = sum(scores[1:])/scores[0] # 평균
    cnt = 0   # 평균을 넘는 학생 수

    # 평균을 넘는 학생 수 구하기
    for i in scores[1:]:
        if i > avg:
            cnt += 1
    
    rate = cnt/scores[0]*100
    print(f"{rate:.3f}%")  # 소수점 셋째 자리까지 출력