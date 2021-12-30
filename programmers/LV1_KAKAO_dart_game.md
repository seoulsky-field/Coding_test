< 코드 작성 전 생각 >
- split을 이용할 경우 무엇을 기준으로 할 것인지 애매함
- str를 마주하면 (!isdigit()) 앞에 부분을 숫자로 어떤 리스트에 옮기고 S냐 D냐 T냐 #이냐 *이냐에 따라 처리 다르게 함
- S면 해당 숫자를 그대로 옮김, D면 ** 2 값으로 옮김, T면 ** 3 값으로 옮김, *이면 [-1], [-2] 값에 *2 (해당 리스트 len 보고 [-2]는 생략), #이면 [-1]에 * (-1)

< 1차 작성 코드 >
def solution(dartResult):
    answer = 0
    numbers = []

    for idx, value in enumerate(dartResult):
        if not value.isdigit():
            if value == "S":
                number = int(dartResult[:idx])
                numbers.append(number)
            elif value == "D":
                number = int(dartResult[:idx])
                numbers.append(number ** 2)
            elif value == "T":
                number = int(dartResult[:idx])
                numbers.append(number ** 3)
            elif value == "*":
                numbers[-1] *= 2
                if len(numbers) > 1:
                    numbers[-2] *= 2
            else:
                numbers[-1] *= -1
            
            dartResult = dartResult[idx+1:]
        
    answer = sum(numbers)

    return answer


-> ValueError: invalid literal for int() with base 10: '2D3'
-> 오류 이유 : dartResult를 자른 것 때문에 idx가 범위대로 자르더라도 숫자만을 자르지 않고 문자를 포함해서 자르게 됨!


< 2차 작성 코드 >
def solution(dartResult):
    answer = 0
    numbers = []

    for value in dartResult:
        if not value.isdigit():
            idx = dartResult.index(value)
            if value == "S":
                number = int(dartResult[:idx])
                numbers.append(number)
            elif value == "D":
                number = int(dartResult[:idx])
                numbers.append(number ** 2)
            elif value == "T":
                number = int(dartResult[:idx])
                numbers.append(number ** 3)
            elif value == "*":
                numbers[-1] *= 2
                if len(numbers) > 1:
                    numbers[-2] *= 2
            else:
                numbers[-1] *= -1
            
            dartResult = dartResult[idx+1:]
        
    answer = sum(numbers)

    return answer

