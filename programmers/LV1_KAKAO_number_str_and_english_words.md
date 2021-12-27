< 코드 작성 전 생각 >
- replace 메소드를 적극적으로 이용하면 되지 않을까?
- 또는 딕셔너리를 이용한 방법. 

< 1차 코드 >
def solution(s):
    answer = 0
    s = s.replace('zero', '0')
    s = s.replace('one', '1')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')
    answer = int(s)
    return answer

-> 해당 풀이로 문제풀이가 되긴 하지만 너무 비효율적으로 보임 
-> 딕셔너리와 for문을 이용해보자!


< 2차 코드 >
def solution(s):
    answer = 0
    numNeng = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for key, value in numNeng:
        s = s.replace(key, value)
    
    answer = int(s)
    return answer

-> ValueError : too many values to unpack (expected 2) error 발생

< 3차 코드 >
def solution(s):
    answer = 0
    numNeng = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    for key in numNeng:
        s = s.replace(key, numNeng[key])
    
    answer = int(s)
    return answer

-> 딕셔너리 사용 미숙으로 인한 for문 잘못 지정 수정
-> 해당 코드로도 가능하다!