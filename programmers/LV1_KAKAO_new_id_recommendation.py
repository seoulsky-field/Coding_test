def solution(new_id):
    answer = ''
    
    for string in new_id:
        if string.isupper():
            answer += string.lower()
        else:
            answer += string
    
    for string in answer:
        if string.islower() or string.isdigit() or string == '.' or string == '-' or string == '_':
            continue
        else:
            answer = answer.replace(string, '')
    
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            answer = answer[0:i] + '*' + answer[i+1:]
    
    answer = answer.replace('*', '')

    
    while len(answer) != 0 and (answer[0] == '.' or answer[-1] == '.'):
        if len(answer) != 0 and answer[0] == '.':
            answer = answer[1:]
        
        if len(answer) != 0 and answer[-1] == '.':
            answer = answer[0:len(answer)-1]
    
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[0:15]
        while answer[-1] == '.':
            answer = answer[0:len(answer)-1]
    
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer

example = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]

for value in example:
    value = solution(value)
    print(value)