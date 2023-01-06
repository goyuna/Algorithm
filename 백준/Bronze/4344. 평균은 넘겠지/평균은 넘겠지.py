c = int(input())    # 테스트케이스 개수

for _ in range(c):
    scores = list(map(int, input().split()))    # 학생 점수리스트
    n = scores[0]   # 학생 수
    sum = 0         # 성적 합계
    cnt = 0        # 평균을 넘는 학생 수

    # 평균 구하기
    for i in scores[1:]:
        sum += i
    avg = sum/(len(scores)-1)

    # 평균을 넘는 학생 수 구하기
    for i in scores[1:]:
        if i > avg:
            cnt += 1

    print(f"{(cnt/(len(scores)-1)*100):.3f}%")  # 소수점 셋째 자리까지 출력