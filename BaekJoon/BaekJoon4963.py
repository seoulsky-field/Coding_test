import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, 1, 1, -1, -1, -1]    # x방향 움직임
dy = [1, -1, 1, 0, -1, 1, 0, -1]    # y방향 움직임
queue = deque()    # BFS 탐색에 쓰일 queue 선언

def BFS():
    while queue:    # queue에 값이 존재하지 않을 때까지 반복
        x, y = queue.popleft()    # 입력되어 있는 위치를 호출
        for idx in range(8):    # 대각선 포함 8방향에 대해 탐색
            mx = x + dx[idx]    # x좌표 이동
            my = y + dy[idx]    # y좌표 이동
            if 0 <= mx < h and 0 <= my < w and island_map[mx][my] == 1:    # 범위 내의 좌표이면서 섬일 경우
                queue.append((mx, my))    # queue에 해당 위치 저장
                island_map[mx][my] = 0    # 탐색한 좌표에 대해 0으로 값 지정

while True:    # break 전까지 무한 반복
    w, h = map(int, input().split())    # 높이와 너비 입력
    if w == 0 and h == 0:    # 모두 0이라면 종료
        break
    island_map = list(list(map(int, input().split())) for _ in range(h))    # 섬에대한 지도 입력
    island = 0    # 섬의 개수 선언 및 초기화

    for i in range(h):    # 높이에 대해 반복(=행 개수)
        for j in range(w):    # 너비에 대해 반복(=열 개수)
            if island_map[i][j] == 1:    # 해당 좌표가 섬일 경우
                queue.append((i, j))    # queue에 해당 위치 저장
                island_map[i][j] == 0    # 해당 위치에 대해 0으로 값 지정
                BFS()    # BFS 알고리즘 시작
                island += 1    # BFS 알고리즘이 끝나면 섬 카운팅이 끝나므로 1 추가
    
    print(island)    # 섬의 개수 출력