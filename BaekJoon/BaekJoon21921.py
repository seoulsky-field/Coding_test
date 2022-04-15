# 21921번 블로그(22. 04. 15. 금)
# https://www.acmicpc.net/problem/9536

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitor = list(map(int, input().split()))
max_count = 0
how_long = 0
sum_count = sum(visitor[:X])

for idx in range(N-X+1):
    if sum_count > max_count:
        max_count = sum_count
        how_long = 1
    elif sum_count == max_count:
        how_long += 1
    
    if X+idx != N:
        sum_count = sum_count - visitor[idx] + visitor[X+idx]

print(f'{max_count}\n{how_long}') if max_count != 0 else print('SAD')