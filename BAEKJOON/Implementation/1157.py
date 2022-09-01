'''
1157. 단어공부
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

word = input().upper() # 입력받은 단어를 대문자로 변환하여 저장 
word_list = list(set(word)) # 중복된 문자값 제거 후 비교변수에 저장 
cnt = []
for i in word_list: 
    count = word.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1: #cnt에서 max값이 1이상이라면
    print("?")  # ?출력
else:
    print(word_list[(cnt.index(max(cnt)))]) # cnt의 max값을 가진 index값을 찾아 word_list에서 index에 해당하는 값 출력