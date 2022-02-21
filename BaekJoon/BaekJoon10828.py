''' 시간 초과 풀이 '''
# rep_num = int(input())
# stack = []

# for _ in range(rep_num):
#     command = input()
#     if "push" in command:
#         stack.append(int(command.split(" ")[1]))
#     elif "pop" in command:
#         if len(stack) == 0:
#             print(f"{-1}")
#         else:
#             print(stack.pop())
#     elif "size" in command:
#         print(len(stack))
#     elif "empty" in command:
#         if len(stack) == 0:
#             print(f"{1}")
#         else:
#             print(f"{0}")
#     else:
#         if len(stack) == 0:
#             print(f"{-1}")
#         else:
#             print(stack[-1])


import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

rep_num = int(input())    # 명령어 개수 입력
stack = []    # stack list

for _ in range(rep_num):    # 명령어 개수만큼 반복
    command = input()    # 명령어 한 줄 입력
    if "push" in command:    # 명령어가 push라면
        stack.append(int(command.split(" ")[1]))    # 공백을 기준으로 split 한 후, 1번 인덱스 값을 int로 변환하여 stack에 저장
    elif "pop" in command:    # 명령어가 pop라면
        if len(stack) == 0:    # 빈 stack이라면 -1 출력
            print(f"{-1}")
        else:    # 빈 stack이 아니라면 stack의 마지막 값 추출 및 출력
            print(stack.pop())
    elif "size" in command:    # 명령어가 size라면
        print(len(stack))    # stack의 크기 출력
    elif "empty" in command:    # 명령어가 empty라면
        if len(stack) == 0:    # 빈 stack이라면 1 출력
            print(f"{1}")
        else:    # 빈 stack이 아니라면 0 출력
            print(f"{0}")
    else:    # 명령어가 top라면
        if len(stack) == 0:    # 빈 stack이라면 -1 출력
            print(f"{-1}")
        else:    # 빈 stack이 아니라면 stack의 마지막 값 출력
            print(stack[-1])
