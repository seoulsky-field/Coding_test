import sys  # sys.stdin.readline()을 사용하기 위해서 sys module을 import합니다.

T = int(sys.stdin.readline())   # sys.stdin.readline()을 이용해 입력받고 정수형으로 변환합니다.
for i in range(0, T):   # 숫자 T만큼 반복합니다.
    a, b = tuple(int(s) for s in sys.stdin.readline().split(' '))   # 입력받은 두 숫자를 공백으로 분리하고 정수형으로 변환하여 tuple로 담아 두 변수에 두 숫자를 저장합니다.
    print(a + b)    # 계산 결과를 출력합니다.