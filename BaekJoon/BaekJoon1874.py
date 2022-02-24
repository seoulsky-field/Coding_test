import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

last_in = 1
result = []
num_list = []

FLAG = True

T = int(input())    # 테스트 케이스 개수를 입력

for _ in range(T):    # 테스트 케이스 개수만큼 반복
    num = int(input())    # 정수 입력
    
    while last_in <= num:    # 마지막 입력된 정수가 num이 될 때까지 반복
        num_list.append(last_in)    # 정수를 stack에 저장
        # print("input >>>", last_in)
        result.append('+')    # stack에 쌓으므로 '+' 저장
        last_in += 1    # 입력할 정수가 다음 숫자로 넘어감
        # print(last_in)

    # while num in num_list:
    if num_list[-1] == num:    # 내려올 때는 무조건 한 칸씩 내려와야 함
        result.append('-')    # pop이므로 '-' 저장
        num_list.pop()    # 마지막 값 pop
        # print("out >>>", last_out)
    else:    # 여러 칸 내려온다면?
        FLAG = False    # 불가능!
        break    # for문 종료

if FLAG:
    for value in result:
        print(value)
else:
    print('NO')
    