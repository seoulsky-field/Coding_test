< 코드 작성 전 생각 >
- N크기의 list 생성. 이름은 count 정도
- stages에 들어있는 사용자가 도전 중인 스테이지 값 - 1을 인덱스로 하여 count에 1증가
- failure_rate list 생성. 1스테이지(0번째 인덱스)부터 count[0] / sum 해당 인덱스부터 끝까지의 값들 (if else를 이용해서 0처리와 예외처리가 필요할듯!)
- 마지막 정렬은 max값을 이용하여 index 반환. 아마도 max가 동일하다면 작은 인덱스부터 반환하지 않을까? 하는 원리 이용

< 1차 코드 >
def solution(N, stages):
    answer = []
    count = []
    failure_rate = []
    
    for i in range(0, N):
        count.append(0)
        failure_rate.append(0)
    
    for value in stages:
        count[value-1] += 1
    
    for idx, value in enumerate(count):
        addition = sum(count[idx:len(count)])
        if addition != 0:
            failure_rate[idx] = count[idx] / addition
    
    for idx, value in enumerate(failure_rate):
        answer.append(failure_rate.index(max(failure_rate)) + 1)
        failure_rate[failure_rate.index(max(failure_rate))] = -1
    
    return answer

- 문제점 : list index out of range 나타남.
- 해결 방법 : stages에 N + 1 값이 들어갈 수 있으므로 조정


< 2차 코드 >
- 1. 처음 for문에서 N을 N + 1로 조정
- 2. count와 failure_rate의 enumerate도 [0:N] 범위로 조정

def solution(N, stages):
    answer = []
    count = []
    failure_rate = []
    
    for i in range(0, N + 1):
        count.append(0)
        failure_rate.append(0)
    
    for value in stages:
        count[value-1] += 1
    
    for idx, value in enumerate(count[0:N]):
        addition = sum(count[idx:len(count)])
        if addition != 0:
            failure_rate[idx] = count[idx] / addition
    
    for idx, value in enumerate(failure_rate[0:N]):
        answer.append(failure_rate.index(max(failure_rate)) + 1)
        failure_rate[failure_rate.index(max(failure_rate))] = -1
    
    return answer
