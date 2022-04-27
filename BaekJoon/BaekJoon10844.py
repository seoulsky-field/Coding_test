# 10844번 쉬운 계단 수(22. 04. 26. 화)
# https://www.acmicpc.net/problem/10844
import sys
input = sys.stdin.readline

N = int(input())
dp = list([0] * 10 for _ in range(N))
dp[0] = [0] + [1] * 9

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1]) % 1000000000)