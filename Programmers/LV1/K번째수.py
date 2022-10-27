#https://school.programmers.co.kr/learn/courses/30/lessons/42748
#정렬

def solution(array, commands):
    answer = []
    new_array = []
    
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1 : commands[i][1]]
        new_array = sorted(new_array)

        answer.append(new_array[commands[i][2]-1])

    return answer

print(solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))