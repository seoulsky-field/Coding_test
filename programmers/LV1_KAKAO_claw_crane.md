< 코드 작성 전 생각 >
예시는 인형뽑기 배열 맨 위의 행부터 입력됨
for for : 이중 for문. 첫 번째는 moves 길이만큼, 두 번째는 board의 행 개수만큼
moves.pop가 board[][]의 값과 같은지 확인
-> 같다면 board[][] = 0, result += 2
-> 같지 않다면 moves.append(pop한 값) ,board[][] = 0, dull[].append(board[][])


< 1회 시도 코드 >
def solution(board, moves):
    dolls = []
    answer = 0
    
    for value in moves:
        for row in board:
            if row[value-1] == 0:
                continue
            else:
                doll = lambda x : dolls.pop() if (len(dolls) != 0) else 0
                if row[value-1] == doll:
                    answer += 2
                else:
                    dolls.append(doll)
                    dolls.append(row[value-1])
                row[value-1] = 0
                break
    
    return answer

-> 기댓값 4가 아닌 0이 나옴

< 2회 시도 코드 >
- 수정사항 : lambda의 사용 미숙으로 if/else 이용
- doll이 0인 경우도 추가되므로 해당 부분 수정

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