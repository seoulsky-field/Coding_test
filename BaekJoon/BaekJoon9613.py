from itertools import combinations    # 수학에서의 조합을 사용할 수 있게 해주는 library
from fractions import Fraction    # 분수식으로 표현할 수 있게 해주는 library
import sys
input = sys.stdin.readline    # 시간 초과 error를 해결하기 위한 input함수 재정의

n = int(input())    # 테스트 케이스의 개수
for _ in range(n):
    answer = 0    # 정답을 저장하는 변수
    num, *numbers = map(int, input().strip().split(' '))    # 개수와 숫자들을 모두 입력받는 방법

    for (num1, num2) in list(combinations(numbers, 2)):    # numbers에서 2개씩 뽑는 조합을 진행
        f = Fraction(num1, num2)    # num1과 num2를 분수식으로 표현 (이 때, 기약분수로 표현됨)
        answer += num1 // f.numerator    # num1을 분자로 나눈다면 GCD (num2을 분모로 나눠도 동일)

    print(answer)    # 정답 출력