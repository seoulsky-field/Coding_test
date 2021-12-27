# def solution(s):
#     answer = 0
#     s = s.replace('zero', '0')
#     s = s.replace('one', '1')
#     s = s.replace('two', '2')
#     s = s.replace('three', '3')
#     s = s.replace('four', '4')
#     s = s.replace('five', '5')
#     s = s.replace('six', '6')
#     s = s.replace('seven', '7')
#     s = s.replace('eight', '8')
#     s = s.replace('nine', '9')
#     answer = int(s)
#     return answer

def solution(s):
    answer = 0
    numNeng = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    for key in numNeng:
        s = s.replace(key, numNeng[key])
    
    answer = int(s)
    return answer

example = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]

for value in example:
    print(solution(value))