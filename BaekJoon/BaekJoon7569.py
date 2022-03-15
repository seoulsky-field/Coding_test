# 문제 유형 : 그래프 탐색
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())    # 상자의 크기 (M, N)과 높이(H) 입력
tomato_boxes = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]    # 3차원 토마토 상자 입력 (channel이은 (H, N, M)순)
visit = deque()    # BFS 탐색 좌표 저장 공간

dh = [0, 0, 0, 0, 1, -1]    # H channel이 이동 거리
dn = [0, 0, 1, -1, 0, 0]    # N channel이 이동 거리
dm = [1, -1, 0, 0, 0, 0]    # M channel이 이동 거리

def BFS():    # BFS 탐색
    while visit:    # 탐색할 좌표가 존재하지 않을 때까지 반복
        h, n, m = visit.popleft()    # BFS에 의하여 FIFO을 적용

        for d in range(6):    # 총 이동 가능한 방향이 여섯 방향이므로 여섯 번 반복
            nh = h + dh[d]    # H channel이 이동
            nn = n + dn[d]    # N channel이 이동
            nm = m + dm[d]    # M channel이 이동

            # 조건 : 각 channel이에 대해 이동한 좌표가 주어진 좌표 안에 존재하며 토마토가 익지 않은 경우
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and tomato_boxes[nh][nn][nm] == 0:
                tomato_boxes[nh][nn][nm] = tomato_boxes[h][n][m] + 1    # 몇 번 이동하여 익었는지 기록
                visit.append((nh, nn, nm))    # 토마토가 익었으므로 좌표 저장


for h in range(H):    # H부터 channel이 시작하므로 for문도 H부터 시작
    for n in range(N):    # 다음은 N channel이
        for m in range(M):    # 다음은 M channel이
            if tomato_boxes[h][n][m] == 1:    # 토마토가 익었다면 해당 좌표 저장
                visit.append((h, n, m))

BFS()    # 탐색 진행
answer = 0    # 정답을 담을 변수
flag = True    # 탐색 불가능 판별

for h in range(H):    # 마찬가지로 H부터 시작
    for n in range(N):    # N번 반복
        for m in range(M):    # M번 반복
            if tomato_boxes[h][n][m] == 0:    # 탐색 후 익지 않은 토마토가 존재할 경우
                flag = False    # 전체가 익을 수 없으므로 탐색 불가능 선정 후 반복 종료
                break
            answer = max(answer, tomato_boxes[h][n][m])    # 가장 마지막으로 익은 토마토가 몇 번째 회차에서 익었는지 확인

print(answer - 1) if flag else print(-1)    # 처음 탐색을 시작할 때 0이 아닌 1로 시작하므로 나중에 1을 제외하고 익지 않은 토마토가 존재하면 -1 출력