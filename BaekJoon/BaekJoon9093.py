import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

num = int(input())    # 테스트 케이스 개수를 입력
sentence = []    # 테스트 케이스를 저장받을 리스트 선언

for _ in range(num):    # 테스트 케이스 개수만큼 반복
    sentence = input().strip().split(' ')    # 테스트 케이스를 입력받고, 공백으로 분리
    for idx, value in enumerate(sentence):    # enumerate로 index와 value를 받아오면서
        sentence[idx] = value[::-1]    # value의 값을 뒤집어서 저장
    print(' '.join(sentence))    # 출력물은 공백을 기준으로 리스트를 합침