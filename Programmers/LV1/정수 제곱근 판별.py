#
from math import sqrt   #sqrt : 제곱근

def solution(n):
    if sqrt(n) % 1 == 0:
        return int(sqrt(n) + 1) **2
    else:
        return -1

print(solution(121))

