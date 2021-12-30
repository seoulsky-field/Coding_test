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


example = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]
for idx, value in enumerate(example):
    print(f"예제 {idx+1}번 : {solution(value)}")