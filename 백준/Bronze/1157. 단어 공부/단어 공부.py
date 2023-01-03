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