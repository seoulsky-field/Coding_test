< 구현 전 생각 >
- 문자열 n개 단위로 자르는 변수 n필요
- for문 생성, n의 영향을 받음, 점프는 n크기만큼
- for문에서 인덱스별로 시작하는데, 처음 문자를 0번째 인덱스부터 n-1번째 인덱스까지 지정
- 다음 문자가 이전 문자와 같은지 비교. 같다면 count 증가. 다르면 count에 맞게 리스트에 append


< 1차 코드 >
def solution(s):
    answer = len(s)
    divisor = []
    for i in range(1, len(s)+1):
        if len(s) % i == 0:
            divisor.append(i)
    
    for n in divisor:
        tmp = []
        count = 1
        txt = s[0:n]
        for idx in range(n, len(s)+1-n, n):
            if txt == s[idx : 2*idx]:
                count += 1
            else:
                if not count == 1:
                    tmp.append(str(count))
                tmp.append(txt)
                txt = s[idx : 2*idx]
                count = 1
        txt = ''.join(tmp)
        if len(txt) < answer:
            answer = len(txt)
                
    return answer

-> 에러 : 모든 실행 결괏값이 0이 나옴


< 2차 코드 >
def solution(s):
    answer = len(s)
    divisor = []
    for i in range(1, len(s)):
        if len(s) % i == 0:
            divisor.append(i)
    
    for n in divisor:
        tmp = []
        count = 1
        txt = s[0:n]
        for idx in range(n, len(s)+1-n, n):
            if txt == s[idx : idx+n]:
                count += 1
            else:
                if not count == 1:
                    tmp.append(str(count))
                tmp.append(txt)
                txt = s[idx : idx+n]
                count = 1
        if not count == 1:
            tmp.append(str(count))
            tmp.append(txt)
        txt = ''.join(tmp)
        if len(txt) < answer:
            answer = len(txt)
                
    return answer

- 수정 사항
- 문자열 split할 때 콤마가 아니라 세미콜론임!
-> 결괏값이 0은 아니지만 제대로 안나옴


< 3차 코드 >
def solution(s):
    answer = len(s)
    
    for n in range(1, len(s)):
        tmp = []
        count = 1
        txt = s[0:n]
        idx = 0
        for idx in range(n, len(s)+1, n):
            if txt == s[idx : idx+n]:
                count += 1
            else:
                if not count == 1:
                    tmp.append(str(count))
                tmp.append(txt)
                txt = s[idx : idx+n]
                count = 1
        
        if not count == 1:
            tmp.append(str(count))
            tmp.append(txt)
        
        if len(s) % n != 0:
            tmp.append(s[idx:])
        
        txt = ''.join(tmp)

        if len(txt) < answer:
            answer = len(txt)
                
    return answer

- 수정 사항
- 약수로만 하면 안됨.
- 또한 약수가 아닐경우 뒤에 남는 문자열도 추가해주어야 함!