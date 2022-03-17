import sys
input = sys.stdin.readline

A, B, C, D = input().split()    # A부터 D까지 입력
print(int(A+B) + int(C+D))    # A와 B를 문자열로 합친 후 정수로 변환, C와 D도 마찬가지로 한 후 두 수를 더함