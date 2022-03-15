import sys
input = sys.stdin.readline

while True:    # 문장이 들어오지 않을 때까지 반복
    answer = [0, 0, 0, 0]    # 순서대로 소문자, 대문자, 숫자, 공백 저장
    sentence = input().rstrip('\n')    # 문장 입력 (줄바꿈 문자 제거)

    if not sentence:    # 문장이 들어오지 않았다면 종료
        break

    for ch in sentence:    # 문장의 각각의 단어를 판별
        if ch.islower():    # 단어가 소문자일 경우 count
            answer[0] += 1
        elif ch.isupper():    # 단어가 대문자일 경우 count
            answer[1] += 1
        elif ch.isdigit():    # 단어가 숫자일 경우 count
            answer[2] += 1
        elif ch.isspace():    # 단어가 공백일 경우 count
            answer[3] += 1

    print(*answer)    # 정답 출력
