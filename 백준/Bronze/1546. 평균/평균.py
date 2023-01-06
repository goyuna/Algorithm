n = int(input())
grade = list(map(int, input().split()))
new_grade = []

for i in range(n):
    new_grade.append(grade[i]/max(grade)*100)

print(sum(new_grade)/n)