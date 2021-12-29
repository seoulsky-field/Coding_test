< 코드 작성 전 생각 >
- arr1을 암호화, arr2를 암호화하고 두 암호화를 합치자!
- arr에서 각각의 숫자를 암호화 할 때는 for i in range(n, -1, -1)로 해서 2의 n승부터 2의 0승까지 뺄 때 0보다 크고 작은지 판별
- 이후 arr1 암호화와 arr2 암호화를 더함 if 암호화 한 arr1[i] == '#' or 암호화 한 arr2[i] == '#' 이면 '#'으로..

< 1차 코드 >
def solution(n, arr1, arr2):
    answer = []
    encrypt_arr1 = []
    encrypt_arr2 = []
    
    for value in arr1:
        c = ""
        for i in range(n-1, -1, -1):
            if value - 2**i >= 0:
                value -= 2**i
                c += "#"
            else:
                c += " "
        encrypt_arr1.append(c)
    
    for value in arr2:
        c = ""
        for i in range(n-1, -1, -1):
            if value - 2**i >= 0:
                value -= 2**i
                c += "#"
            else:
                c += " "
        encrypt_arr2.append(c)
    
    for value in list(zip(encrypt_arr1, encrypt_arr2)):
        c = ""
        for i in range(0, n):
            if value[0][i] == "#" or value[1][i] == "#":
                c += "#"
            else:
                c += " "
        answer.append(c)
            
    
    return answer