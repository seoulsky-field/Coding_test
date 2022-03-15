import sys
input = sys.stdin.readline

answer = []    # 정답을 저장할 리스트 생성
word = input().strip()    # 단어 입력

for i in range(ord('a'), ord('z')+1):    # a부터 z까지 반복
    answer.append(word.find(chr(i)))    # 알파벳의 위치를 단어에서 찾고 정답에 추가 (없을 경우 -1이 자동 추가)

print(*answer)    # 정답 출력