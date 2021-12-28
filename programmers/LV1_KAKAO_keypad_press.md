< 코드 작성 전 생각 >
- 현재 양 엄지 손가락의 위치를 계속 update 해야하고 시작 전 위치도 저장해야 한다.
- for문 value in numbers로 돌린다.
- if문 value in [1, 4, 7]일 경우 "L"
- elif문 value in [3, 6, 9]일 경우 "R"
- else에서 현재 위치 받고 각각의 거리 계산 : abs 메소드 이용하면 될 듯

< 1차 코드 >
def solution(numbers, hand):
    answer = ''
    lThumb = [0, 3]
    rThumb = [2, 3]
    
    for value in numbers:
        if value in [1, 4, 7]:
            lThumb = [0, [1, 4, 7].index(value)]
            answer += 'L'
        elif value in [3, 6, 9]:
            rThumb = [2, [3, 6, 9].index(value)]
            answer += 'R'
        else:
            checkPoint = [1, [2, 5, 8, 0].index(value)]
            lDistance = abs(lThumb[0] - checkPoint[0]) + abs(lThumb[1] - checkPoint[1])
            rDistance = abs(rThumb[0] - checkPoint[0]) + abs(rThumb[1] - checkPoint[1])
            
            if lDistance > rDistance:
                rThumb = [1, checkPoint[1]] 
                answer += 'R'
            elif lDistance < rDistance:
                lThumb = [1, checkPoint[1]]
                answer += 'L'
            else:
                if hand == 'left':
                    lThumb = [1, checkPoint[1]]
                    answer += 'L'
                else:
                    rThumb = [1, checkPoint[1]] 
                    answer += 'R'
            
    
    return answer


