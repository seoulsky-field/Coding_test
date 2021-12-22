< 코드 작성 전 생각 >
1단계
-> 대문자를 소문자로 치환하는 메소드가 있다면 사용
-> 없다면 for문을 통해 ASCII코드의 대문자에 해당하는 문자라면 특정 값을 빼어 저장

2단계
-> for문으로 각 문자를 접근하여 ASCII 코드 비교 & -_. 중 하나인지 비교. 아니면 제거 (효율적 코드는 아닌 듯 해보임)

3단계
-> for을 len(string)-1만큼 반복, i번째 인덱스와 i+1번째 인덱스를 비교해 둘 다 마침표라면 i번째 인덱스를 위 세 가지 기호 외에 다른 기호로 치환
-> 이후 그 기호를 제거

4단계
-> [0] 또는 [-1]을 이용하여 비교 및 제거

5단계
-> len(string) == 0이라면 new_id = "a" 이용

6단계
-> len(string) >= 16이라면 string = string[0:15] 이용, if string[-1] = '.' 이라면 . 제거

7단계
-> len(string) <= 2이라면 string += string[-1]을 반복 (while문 이용)


< 1차 코드 >
def solution(new_id):
    answer = new_id
    
    for i in range(len(answer)):
        if answer[i] >= 65 and answer[i] <= 90:
            answer[i] += 32
    
    for i in range(len(answer)):
        if answer[i] >= 97 and answer[i] <= 122:
            continue
        elif answer[i] >= 48 and answer[i] <= 57:
            continue
        elif answer[i] == '.' or answer[i] == '-' or answer[i] == '_':
            continue
        else:
            answer[i] = ""
    
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            answer[i] == '*'
    answer.replace('*', '')
    
    while (answer[0] == '.' or answer[-1] == '.'):
        if answer[0] == '.':
            answer[0] == ''
        
        if answer[-1] == '.':
            answer[-1] == ''
    
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[0:15]
    
    while (len(answer) <= 2):
        answer += answer[-1]
    
    return answer

-> string의 크기 비교 불가 에러 발생

< 2차 코드 >
- 수정사항 : int로 변환하면 가능할지 실행

def solution(new_id):
    answer = new_id
    
    for i in range(len(answer)):
        if int(answer[i]) >= 65 and int(answer[i]) <= 90:
            answer[i] = str(int(answer[i]) + 32)
    
    for i in range(len(answer)):
        if int(answer[i]) >= 97 and int(answer[i]) <= 122:
            continue
        elif int(answer[i]) >= 48 and int(answer[i]) <= 57:
            continue
        elif answer[i] == '.' or answer[i] == '-' or answer[i] == '_':
            continue
        else:
            answer[i] = ""
    
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            answer[i] == '*'
    answer.replace('*', '')
    
    while (answer[0] == '.' or answer[-1] == '.'):
        if answer[0] == '.':
            answer[0] == ''
        
        if answer[-1] == '.':
            answer[-1] == ''
    
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[0:15]
    
    while (len(answer) <= 2):
        answer += answer[-1]
    
    return answer

-> int로 변환 불가능 에러 발생

< 3차 코드 >
- 위의 에러들과 string index out of range, while문 무한 반복등의 에러 발생을 이유로
- programmers 창이 아닌 VS Code에서 print를 이용해 문제 파악 및 일일이 실행하여 에러들을 잡음
- 수정사항
- 1. 대소문자 변환을 isuppper(), lower() 메소드 사용
- 2. 마찬가지로 islower(), isdigit() 등의 메소드 사용으로 소문자 및 숫자인지 파악

def solution(new_id):
    answer = ''
    
    for i in range(len(new_id)):
        if new_id[i].isupper():
            answer += new_id[i].lower()
    
    for i in range(len(answer)):
        if answer[i].islower() or answer[i].isdigit() or answer[i] == '.' or answer[i] == '-' or answer[i] == '_':
            continue
        else:
            answer[i] = ""
    
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            answer[i] == '*'
    answer.replace('*', '')
    
    while (answer[0] == '.' or answer[-1] == '.'):
        if answer[0] == '.':
            answer[0] == ''
        
        if answer[-1] == '.':
            answer[-1] == ''
    
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[0:15]
    
    while (len(answer) <= 2):
        answer += answer[-1]
    
    return answer

-> 문제 : string index out of range
-> 예상 : for문에서 answer[i] = ''를 하고 난 후 index 감소로 인한 문제로 예상

< 4차 코드 >
- 1. isupper()인 경우에만 answer에 추가되므로 해당 부분 수정
- 2. while 문에서 len(answer)가 0일 경우 에러 발생하여 수정
- 3. len(answer)가 16이상일 경우 자르는 부분에서 마지막 문자가 온점일 경우 제거 안되는 부분 수정

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