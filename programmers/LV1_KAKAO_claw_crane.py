def solution(board, moves):
    dolls = []
    answer = 0
    
    for value in moves:
        for row in board:
            if row[value-1] == 0:
                continue
            else:
                doll = 0
                if len(dolls) != 0:
                    doll = dolls.pop()
                
                if row[value-1] == doll:
                    answer += 2
                else:
                    if doll != 0:
                        dolls.append(doll)
                    dolls.append(row[value-1])

                row[value-1] = 0
                break
    
    return answer

# 아래는 실행 예시입니다.
answer = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(answer)