#런타임 에러발생 -> try catch문으로 해결

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break