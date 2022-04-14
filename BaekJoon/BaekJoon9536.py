# 9536번 여우는 어떻게 울지? (22. 04. 14. 목)
# https://www.acmicpc.net/problem/9536

import sys
input = sys.stdin.readline

T = int(input())    # 테스트 케이스 개수 입력

for _ in range(T):    # 테스트 케이스 개수만큼 반복
    animal_sounds = input().split()    # 동물 울음 소리를 입력받고 공백을 기준으로 분리
    sentence = input().strip()    # 문장을 입력받고 줄바꿈 문자 제거

    while sentence != 'what does the fox say?':    # 문장이 ending 문장이 아닐 때까지
        sound = sentence.split()[2]    # 문장의 3번째 단어(index 2)에는 동물 울음 소리가 적혀있으므로 추출
        while sound in animal_sounds:    # 입력받았던 동물 울음 소리들 중 방금 울음 소리가 존재하지 않을 때까지 계속 제거
            animal_sounds.remove(sound)
        sentence = input().strip()    # 문장을 입력받고 줄바꿈 문자 제거
    
    print(' '.join(animal_sounds))    # 제거되고 남은 동물 울음 소리들을 공백을 기준으로 합쳐서 출력