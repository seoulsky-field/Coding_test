import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # A의 크기 N과 명령 횟수 M 입력
A = [list(map(int, input().split())) for _ in range(N)]    # 바구니가 있는 전체 칸 초기값 저장
move_x = [0, -1, -1, -1, 0, 1, 1, 1]    # row의 방향별 증감
move_y = [-1, -1, 0, 1, 1, 1, 0, -1]    # col의 방향별 증감
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]   # 구름 위치 저장 및 초기 설정
check = [(-1, -1), (-1, 1), (1, 1), (1, -1)]    # 대각선 방향에 있는 바구니에 담긴 물의 존재 확인을 위한 x, y 이동 좌표

for _ in range(M):
    d, s = map(int, input().split())    # 이동 정보 입력
    moved_clouds = []    # 이동한 구름의 좌표들이 저장

    for _ in range(len(clouds)):    # 구름이 존재할 때까지 
        x, y = clouds.pop()    # 구름의 좌표를 대입
        new_x = (x + move_x[d-1] * s) % N    # 구름 x좌표 이동
        new_y = (y + move_y[d-1] * s) % N    # 구름 y좌표 이동 
        moved_clouds.append((new_x, new_y))    # 새 구름의 좌표를 저장
        A[new_x][new_y] += 1    # 새 구름이 위치한 곳에 존재하는 바구니에 물 1 증가
    
    for x, y in moved_clouds:    # 이동한 구름의 좌표를 호출    
        for dx, dy in check:    # 각 이동 좌표를 호출
            check_x = x + dx    # 대각선 x방향 좌표 도출
            check_y = y + dy    # 대각선 y방향 좌표 도출
            if 0 <= check_x < N and 0 <= check_y < N and A[check_x][check_y]:    # 대각선 좌표가 A에 존재하고 물이 존재한다면
                A[x][y] += 1    # 이동한 구름이 위치한 곳에 물복사
    
    for i in range(N):    # x탐색 (row)
        for j in range(N):    # y탐색 (col)
            if A[i][j] >= 2 and (i, j) not in moved_clouds:    # 물의 양이 2가 넘고 구름이 존재했던 곳이 아니라면
                clouds.append((i, j))    # 구름 생성
                A[i][j] -= 2    # 물의 양 2 감소

print(sum(sum(value) for value in A))    # 정답 출력