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

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] , "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))