#https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    sums = []
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            sums.append(sum)
    
    sums.sort()
    for k in sums:
        if k not in answer:
            answer.append(k)

    return answer

print(solution([2,1,3,4,1]))

#---------다른 사람 풀이 ---------
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))