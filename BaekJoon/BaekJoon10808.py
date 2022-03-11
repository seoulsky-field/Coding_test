import sys
input = sys.stdin.readline

S = input().strip()    # 단어 입력
answer = [0] * 26    # count할 리스트 생성

for ch in S:
    answer[ord(ch)-97] += 1    # 해당 단어를 ASCII 코드 표에 의거하여 숫자로 변경 후 1증가

print(*answer)    # 정답 출력