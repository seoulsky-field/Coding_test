import sys
input = sys.stdin.readline

stair_num = int(input())    # 계단 개수 입력
stairs = []    # 각 계단별 점수 저장할 배열
dp = [0] * (stair_num + 1)    # 각 계단까지 최고 점수 저장할 배열
for _ in range(stair_num):    # 계단 개수만큼 계단 점수 입력 및 저장
    stairs.append(int(input()))

if stair_num == 1:
    print(stairs[0])
elif stair_num == 2:
    print(stairs[0] + stairs[1])
else:
    dp[1] = stairs[0]    # 첫 번째 계단에서의 최고 점수 = 첫 계단 점수
    dp[2] = stairs[0]+stairs[1]    # 두 번째 계단에서의 최고 점수 = 첫 계단 + 두 번째 계단
    dp[3] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])    # 

    for i in range(3, stair_num+1):
        # 전전 계단까지의 최고 점수 + 지금 계단 점수 vs 전전전 계단까지의 최고 점수 + 전 계단 점수 + 지금 계단 점수
        dp[i] = max(dp[i-2], dp[i-3]+stairs[i-2]) + stairs[i-1]

    print(dp[-1])