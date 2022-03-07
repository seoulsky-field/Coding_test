import sys
from fractions import Fraction    # 기약 분수로 나타내는 Python Library
input = sys.stdin.readline

N = int(input())    # 링의 개수를 입력
rings = list(map(int, input().strip().split(' ')))    # 링의 반지름들을 입력

for i in range(1, N):    # 첫 번째 링을 제외한 나머지 링들에 대해서 진행
    if rings[0] % rings[i] == 0:    # 두 수가 정수꼴로 나눠지면
        print(str(int(rings[0]/rings[i])) + '/' + '1')    # 분모가 1인 분수꼴로 표현 
    else:    # 두 수가 정수꼴로 나눠지지 않는다면
        print(Fraction(rings[0], rings[i]))    # Fraction을 이용해 분수로 표현
