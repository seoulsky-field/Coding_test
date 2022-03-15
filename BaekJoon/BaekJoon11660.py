# 문제 유형 : DP (Dynamic Programming)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 표의 크기와 횟수 입력
table = [list(map(int, input().split())) for _ in range(N)]    # 표 선언 및 값 초기화
sum_table = [[0] * (N + 1) for _ in range(N + 1)]    # 특정 행, 열까지에 대한 합을 저장할 리스트

for i in range(1, N+1):    # 편의를 위해 1부터 N까지 값이 저장되도록 함 (행 탐색)
    for j in range(1, N+1):    # 편의를 위해 1부터 N까지 값이 저장되도록 함 (열 탐색)
        # 특정 행(i), 열(j)까지의 합 = i행 j-1열까지의 합 + i-1행 j열까지의 합 - i-1행 j-1열까지의 합 + 특정 행, 열 값
        sum_table[i][j] = sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1] + table[i-1][j-1]


for _ in range(M):    # 표의 크기만큼 반복
    x1, y1, x2, y2 = map(int, input().split())    # 시작 좌표와 끝 좌표 입력
    # 특정 좌표 범위의 합 = (큰 행, 큰 열)까지의 합 - (큰 행, 작은 열-1)까지의 합 - (작은 행-1, 큰 열)까지의 합 + (작은 행 - 1, 작은 열 - 1)까지의 합
    print(sum_table[x2][y2] - sum_table[x2][y1-1] - sum_table[x1-1][y2] + sum_table[x1-1][y1-1])
