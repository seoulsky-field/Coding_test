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

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))