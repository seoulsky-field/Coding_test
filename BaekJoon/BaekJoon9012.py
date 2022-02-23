import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

num = int(input())    # 테스트 케이스 개수를 입력
for _ in range(num):    # 테스트 케이스 개수만큼 반복
    sentence = input().strip()    # 괄호 문자열을 입력받고 '\n'문자 제거
    while '()' in sentence:    # 괄호쌍이 문자에 존재하면 계속 반복
        sentence = sentence.replace('()', '')    # 괄호쌍을 없애버림
    print('YES') if sentence == '' else print('NO')    # 괄호쌍이 순서에 맞게 존재했다면 모두 제거되고 그렇지 않다면 남음