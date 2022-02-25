# import sys
# input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

# sentence = list(input().strip())    # 줄바꿈 문자를 제외한 input을 한 글자마다 split
# # print(sentence)    # DEBUGGING
# cursor = len(sentence)    # 문장이 입력되면 cursor는 마지막에 위치
# M = int(input())    # command 개수인 M을 입력

# for _ in range(M):    # command 개수만큼 반복
#     cmd = input().strip()    # cmd를 줄바꿈 문자를 제외하여 입력
#     try:
#         cmd, str = cmd.strip().split(' ')    # 명령어가 P일 경우 split하여 str을 저장
#     except:
#         pass    # 명령어가 P가 아닐 경우 특별한 event가 존재X

#     # print('before: ', cursor)    # DEBUGGING
    
#     if cmd == 'L' and cursor != 0:    # L 명령어 + cursor가 맨 앞이 아니라면 왼쪽으로 한 칸 이동
#         cursor -= 1
#     elif cmd == 'D' and cursor != len(sentence):    # D 명령어 + cursor가 맨 뒤가 아니라면 오른쪽으로 한 칸 이동
#         cursor += 1
#     elif cmd == 'B' and cursor != 0 and len(sentence) != 0:    # B 명령어 + cursor가 맨 앞이 아니라면 cursor 위치의 값 제거
#         # print(sentence)    # DEBUGGING
#         cursor -= 1
#         del sentence[cursor]    # 제거 후 자동으로 값이 들어오므로 cursor 위치를 옮길 필요X
        
#         # print(sentence, cursor)    # DEBUGGING
#     elif cmd == 'P':    # P 명렁어가 입력된 경우 cursor 위치에 str을 저장 한 후, 오른쪽으로 한 칸 이동
#         # if cursor == len(sentence) - 1:
#         #     sentence.insert(cursor + 1, str)
#         # else:
#         sentence.insert(cursor, str)
#         cursor += 1
    
#     # print('after: ', cursor)    # DEBUGGING

# print(''.join(sentence))    # list를 str로 합침

import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

stack_left = list(input().strip())    # 입력받은 문자를 줄바꿈 문자를 제외하여 한 글자씩 리스트에 저장
stack_right = list()    # 커서가 가장 마지막에 있으므로 커서의 우측은 아직까지 없으므로 빈 리스트 생성
M = int(input())    # command 개수 입력

for _ in range(M):    # command 개수만큼 반복
    command = input()    # command 입력
    if command[0] == 'L' and len(stack_left) != 0:    # command가 커서 좌측 한 칸 이동이고, 커서가 가장 좌측에 위치하지 않았다면
        stack_right.append(stack_left.pop())    # 커서를 좌측으로 한 칸 이동 (이 때, 커서가 좌측으로 이동하면서 지나간 값은 stack_right에 저장)
    elif command[0] == 'D' and len(stack_right) != 0:    # command가 커서 우측 한 칸 이동이고, 커서가 가장 우측에 위치하지 않았다면
        stack_left.append(stack_right.pop())    # 커서를 우측으로 한 칸 이동 (마찬가지로, 커서가 우측으로 이동하면서 지나간 값을 stack_left에 저장)
    elif command[0] == 'B' and len(stack_left) != 0:    # command가 커서 위치에 있는 값 제거이고, 커서가 가장 좌측에 위치하지 않았다면
        stack_left.pop()    # 해당 값 제거 (제거이므로 stack_right에 저장하지 않으며 stack_left에서 pop을 진행하였기에 커서가 자동으로 이동되는 효과)
    elif command[0] == 'P':    # command가 커서 위치에 값 추가라면
        stack_left.append(command[2])    # 해당 위치에 문자 추가 (stack_left에 추가했기 때문에 커서가 자동으로 이동되는 효과)

stack_left.extend(stack_right[::-1])    # stack_right에는 원래 문자의 순서가 아닌 거꾸로 저장되어 있으므로 돌려서 stack_left와 합)
print(''.join(stack_left))    # 문자열로 출력하기 위한 join 함수 사용