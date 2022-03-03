import sys
from collections import deque
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

deque_list = deque()    # collections library 중 deque를 사용하면 queue를 시간 안에 구현 가능
N = int(input())    # command 개수 입력

for _ in range(N):    # command 개수만큼 반복
    command = input().split()    # 줄바꿈 문자를 제외하고 공백을 기준으로 분리
    if command[0] == 'push_front':    # 명령어가 push_front일 경우 deque_list의 가장 처음에 값을 추가
        deque_list.appendleft(int(command[1]))
    elif command[0] == 'push_back':    # 명령어가 push_back인 경우 deque_list의 가장 마지막에 값을 추가
        deque_list.append(int(command[1]))
    elif 'pop' in command[0]:    # 명령어가 pop_front 또는 pop_back인 경우
        if len(deque_list) == 0:    # deque_list가 비어있다면 -1을 출력
            print(-1)
        elif 'front' in command[0]:    # 명령어가 pop_front인 경우 가장 처음 값을 pop
            print(deque_list.popleft())
        else:    # 명령어가 pop_back인 경우 가장 마지막 값을 pop
            print(deque_list.pop())
    elif command[0] == 'size':    # 명령어가 size인 경우 deque_list의 size를 출력
        print(len(deque_list))
    elif command[0] == 'empty':    # 명령어가 empty인 경우
        print(1 if len(deque_list) == 0 else 0)    # deque_list가 빈 값이면 1을 출력하고 아니면 0을 출력
    else:    # 명령어가 front 또는 back일 경우
        if len(deque_list) == 0:    # deque_list가 비어있다면 -1을 출력
            print(-1)
        elif command[0] == 'front':    # 명령어가 front일 경우 가장 처음 값을 출력
            print(deque_list[0])
        else:    # 명령어가 back일 경우 가장 마지막 값을 출력
            print(deque_list[-1])
