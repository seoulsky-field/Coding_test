# 1149번 RGB거리(22. 04. 25. 월)
# https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

N = int(input())    # 집의 개수 입력
houses = [list(map(int, input().split())) for _ in range(N)]    # 집의 비용 입력

for idx in range(1, N):
    houses[idx][0] = min(houses[idx-1][1], houses[idx-1][2]) + houses[idx][0]
    houses[idx][1] = min(houses[idx-1][0], houses[idx-1][2]) + houses[idx][1]
    houses[idx][2] = min(houses[idx-1][0], houses[idx-1][1]) + houses[idx][2]

print(min(houses[N-1]))