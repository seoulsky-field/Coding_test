import sys
input = sys.stdin.readline

check = [True] * 1000001    # 입력 최댓값이 1,000,000이므로 0포함 1,000,001개 생성 (소수는 True가 될 변수)
for i in range(2, 1000001 // 2):    # 2부터 입력 최댓값의 절반까지 반복
    if check[i]:    # 값이 소수인 경우
        for j in range(2*i, 1000001, i):    # 해당 소수의 배수를 모두 제거
            check[j] = False

N = -1    # 입력 받을 값을 임의로 초기화
while N != 0:    # 값에 0이 들어올 경우 종료
    N = int(input())    # 짝수 입력

    for i in range(3, int(N // 2) + 1, 2):    # 홀수 값만 탐색하며 값의 절반까지만 탐색
        if check[i] and (check[N-i] and N-i > 2):    # 홀수 소수(상대적으로 작은 수)이면서 값-홀수 소수를 만족시키는 홀수인 소수가 존재할경우 (단, 1이 아닌)
            print(f'{N} = {i} + {N-i}')    # 출력 형식에 맞게 출력
            break