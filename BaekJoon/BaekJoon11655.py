sentence = input()
answer = ''    # 정답 문자 출력

for ch in sentence:    # 각 문자별 반복
    if not ch.isalpha():    # 알파벳이 아닐경우 그대로 출력
        answer += ch
        continue
    new = chr(ord(ch) + 13)
    if ch.isupper():    # 대문자인 경우
        if ord(new) > ord('Z'):    # Z보다 ASCII 값이 크다면
            new = chr(ord(new) - 26)    # 26만큼 빼서 대문자 알파벳 범위내로 조정
        answer += new    # 정답에 해당 문자 추가
        continue
    new = chr(ord(ch) + 13)    # 소문자인 경우 13만큼 뒤로 미룸
    if not new.isalpha():    # 뒤로 미룬 값이 알파벳이 아니라면
        new = chr(ord(new) - 26)    # 아스키 코드 값에 의해 26만큼 당겨서 알파벳 범위내로 조정
    answer += new    # 정답에 해당 문자 추가

print(answer)    # 정답 출력