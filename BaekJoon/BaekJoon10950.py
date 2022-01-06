T = int(input())    # 테스트 케이스의 개수 T를 입력받습니다.
result = [] # 결과를 저장하기 위한 리스트를 생성합니다.
for i in range(0, T):   # 테스트 케이스의 개수만큼 반복합니다.
    a, b = tuple(int(s) for s in input().split(' '))   # 입력받은 두 숫자를 공백으로 분리하고 정수형으로 변환하여 tuple로 담아 두 변수에 두 숫자를 저장합니다.
    result.append(a + b)    # 계산 결과를 리스트에 추가합니다.

for value in result:    # 리스트에 저장된 결과들을 불러옵니다.
    print(value)    # 결과를 출력합니다.