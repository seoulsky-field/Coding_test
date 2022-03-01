import sys
from collections import deque
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

N, K = map(int, input().split())    # 입력을 받을 때 공백을 기준으로 분리한 후 각각을 int 타입으로 변환
num_list = deque(x for x in range(1, N+1))    # number를 1부터 N까지 담고있는 list 생성
result = []    # 결과를 저장하는 list

for _ in range(N):    # N개의 원소를 모두 꺼내므로 N만큼 반복
    num_list.rotate(-K+1)    # deque에 존재하는 rotate 함수를 이용하여 list 회전 (K번째 index를 꺼내므로 회전은 K-1번만 진행)
    result.append(num_list.popleft())    # 가장 좌측에 있는 값을 pop

print('<' + str(result).strip('[]') + '>')    # 예제 출력에 맞게 결과 출력


# 1 2 3 4 5 6 7
# 1 2 4 5 6 7    3
# 1 2 4 5 7      3 6
# 1 4 5 7        3 6 2
# 1 4 5          3 6 2 7
# 1 4            3 6 2 7 5
# 4              3 6 2 7 5 1
#                3 6 2 7 5 1 4
