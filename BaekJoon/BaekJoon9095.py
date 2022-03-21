import sys
input = sys.stdin.readline

# 1 -> 1 / 2 -> 2 / 3 -> 4 / 4 -> 7 / 5 -> 11111, 1112 * 4 / 113 * 3 / 122 * 3 / 23 * 2 : 13
answer = [1, 2, 4]    # 초기 1, 2, 3에 대한 값 저장

for idx in range(3, 11):    # 4부터 11까지 값 채우기 (규칙 이용)
    answer.append(answer[idx-1] + answer[idx-2] + answer[idx-3])

T = int(input())    # 테스트 케이스의 개수
for _ in range(T):    # 테스트 케이스의 개수만큼 반복
    print(answer[int(input())-1])    # 정답 출력
    