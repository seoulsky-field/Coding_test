# 1074번 Z(22. 04. 27. 수)
# https://www.acmicpc.net/problem/1074
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())    # N과 r행, c열 정보를 입력
answer = 0    # 정답이 저장될 변수 선언

while N > 0:    # N이 1이 될 때까지만 반복
    check_r, check_c = (2 ** N)/2, (2 ** N)/2    # 사분면 분할에서 기준이 되는 값 지정
    if r < check_r and c < check_c:    # 제 1 사분면에 위치한 경우
        pass    # 추가적으로 해주어야 할 연산 X
    elif r < check_r and c >= check_c:    # 제 2 사분면에 위치한 경우
        answer += 4 ** (N-1)    # 정답에 4의 N-1승을 더하고
        c -= check_c    # 기준 열 값만큼을 찾는 열 값에서 뺄셈 진행
    elif r >= check_r and c < check_c:    # 제 3 사분면에 위치한 경우
        answer += 2 * 4 ** (N-1)    # 정답에 4의 N-1승의 2배를 더하고
        r -= check_r    # 기준 행 값만큼을 찾는 행 값에서 뺄셈 진행
    elif r >= check_r and c >= check_c:    # 제 4 사분면에 위치한 경우
        answer += 3 * 4 ** (N-1)    # 정답에 4의 N-1승의 3배를 더하고
        r -= check_r    # 기준 행 값만큼을 찾는 행 값에서 뺄셈 진행
        c -= check_c    # 기준 열 값만큼을 찾는 열 값에서 뺄셈 진행

    # print(answer)    # 올바르게 값이 찍히는지 디버깅용 확인 코드
    N -= 1    # 크기를 1/4로 감소 (즉, 해당 사분면을 전체로 보고 진행)

print(answer)    # 정답 출력