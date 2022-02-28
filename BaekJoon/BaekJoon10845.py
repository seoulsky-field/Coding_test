import sys
from collections import deque
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

queue_list = deque()    # collections library 중 deque를 사용하면 queue를 시간 안에 구현 가능
M = int(input())    # command 개수 입력

for _ in range(M):    # command 개수만큼 반복
    command = input().split()    # 줄바꿈 문자를 제외하고 공백을 기준으로 분리
    
    if command[0] == 'push':    # 명령어가 push인 경우
        queue_list.append(command[1])    # push 다음에 존재하는 숫자를 queue에 추가
    elif command[0] == 'pop':    # 명령어가 pop인 경우
        if len(queue_list) == 0:    # 빈 queue라면 -1을 출력
            print(-1)
        else:    # 빈 queue가 아니라면 deque에 존재하는 popleft()를 이용하여 가장 처음 들어온 값을 pop
            print(queue_list.popleft())
    elif command[0] == 'size':    # 명령어가 size인 경우 queue의 길이 출력
        print(len(queue_list))
    elif command[0] == 'empty':    # 명령어가 empty인 경우
        if len(queue_list) == 0:    # 빈 queue라면 1 출력
            print(1)
        else:    # 빈 queue가 아니라면 0 출력
            print(0)
    elif command[0] == 'front':    # 명령어가 front인 경우
        if len(queue_list) == 0:    # 빈 queue라면 -1을 출력
            print(-1)
        else:    # 빈 queue가 아니라면 가장 앞에 있는 값 출력
            print(queue_list[0])
    else:    # 명령어가 back인 경우
        if len(queue_list) == 0:    # 빈 queue라면 -1을 출력
            print(-1)
        else:    # 빈 queue가 아니라면 가장 마지막에 있는 값 출력
            print(queue_list[-1])