# 2805번 나무 자르기 문제 (22. 04. 13. 수)
# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cutting = 0

    for value in trees:
        cut_num = value - mid
        if cut_num > 0:
            cutting += cut_num
    
    print(start, mid, end, cutting)
    
    if cutting >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)