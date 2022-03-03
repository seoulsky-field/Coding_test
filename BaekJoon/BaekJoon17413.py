from audioop import reverse
import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

sentence = input().strip()    # 문장을 입력받는다.
answer = []    # 정답을 입력할 리스트 생성
temp = ''    # <>안에 값이 들어가 있지 않다면 저장할 빈문자열 생성
flag = False    # 해당 문자가 >와 < 사이에 존재한다면 False, <와 >사이에 존재한다면 True

for idx, ch in enumerate(sentence):    # 문장 안에 있는 각각의 문자마다 반복
    if ch == '<':    #  문자가 <인 경우
        if not flag:    # 만약 이전까지 >와 <사이에 존재했었다면
            answer.append(temp[::-1])    # 해당 단어를 거꾸로 반환하여 정답에 저장
            temp = ''    # 빈문자열로 재할당
        answer.append(ch)    # 정답에 < 문자 추가
        flag = True    # <가 시작하므로 flag를 True로 바꿔주어야 함
    elif ch == '>':    # 문자가 > 인 경우
        answer.append(ch)    # 정답에 > 문자 추가
        flag = False    # 다음 문자부터 > 뒤에 해당하므로 False
    elif ch == ' ':    # 문자가 빈칸이라면
        answer.append(temp[::-1])    # temp 속 문자들을 거꾸로 반환하여 정답에 저장
        answer.append(ch)    # 공백 문자도 정답에 저장
        temp = ''    # temp는 다시 빈 단어로 만들어준다.
    else:    # 문자가 일반 문자라면
        if flag:    # flag가 True인 경우. 즉, <와 > 사이에 존재하는 문자일 경우
            answer.append(ch)    # 정답에 문자 바로 추가
        else:    # flag가 False인 경우. 즉, >뒤에 존재하는 문자일 경우
            temp += ch    # temp에 문자 저장
    if idx == len(sentence) - 1:    # 마지막 문자일 경우
        answer.append(temp[::-1])    # temp에 있는 문자 거꾸로 반환하여 정답에 저장

print(''.join(answer))    # 정답을 문자열 형태로 출력
