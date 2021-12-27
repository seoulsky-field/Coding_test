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


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))