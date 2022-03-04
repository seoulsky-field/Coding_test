import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

sticks = input().strip()    # 문장을 입력받는다.
laser_stack = []    # 층또는 레이저가 쌓일 list
answer = 0    # 정답은 0부터 시작

for idx in range(len(sticks)):
    if sticks[idx] == '(':    # 층 또는 레이저가 시작될 경우
        laser_stack.append('(')    # stack에 추가
    else:    # 층이 끝나거나 레이저가 끝난 경우
        laser_stack.pop()    # 층 끝남 및 레이저만 존재한 경우 레이저 제거
        if sticks[idx-1] == '(':    # 즉, 레이저인 경우
            answer += len(laser_stack)    # 레이저가 한 번 발사 될 때 마다 해당 층부터 아래 층까지 조각남
        else:    # 레이저가 아닌 층이 끝난 경우
            answer += 1    # 레이저 두 번이면 쇠 막대기 하나는 세 개로 쪼개지기 때문

print(answer)    # 정답 출력
