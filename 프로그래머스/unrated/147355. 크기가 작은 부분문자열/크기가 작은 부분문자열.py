def solution(t, p):
    answer = 0
    t_slice = [t[i:i+len(p)] for i in range(0, len(t)) if len(t[i:i+len(p)]) == len(p)]
    int_t_slice = list(map(int, t_slice))

    for t in int_t_slice:
        if t <= int(p):
            answer +=1
    
    return answer