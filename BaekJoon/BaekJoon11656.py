import sys
input = sys.stdin.readline
answer = []    # 정답 저장

S = input().rstrip('\n')    # 문자열 입력
for i in range(len(S)):    # 문자열 길이만큼 반복
    answer.append(S[i:])    # 접미사 추출 및 저장

answer.sort()    # 정답을 알파벳 순으로 정렬
print('\n'.join(answer))    # 정답을 줄바꿈 문자를 이용해 출력