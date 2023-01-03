x,y = map(int, input().split(' '))
month =[31,28,31,30,31,30,31,31,30,31,30,31]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
day = 0

for i in range(x-1):
    day += month[i]

day += y-1
day %= 7

print(week[day])