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


example = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
for value in example:
    print(solution(value))