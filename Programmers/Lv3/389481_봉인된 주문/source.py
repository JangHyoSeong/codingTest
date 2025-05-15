def solution(n, bans):
    answer = ''
    bans.sort(key = lambda x : (len(x), x))
    for ban in bans:
        if str_to_num(ban) <= n:
            n += 1
    
    while n > 0:
        n -= 1
        answer += chr(n % 26 + ord("a"))
        n //= 26
    
    return answer[::-1]

def str_to_num(string):
    num = 0
    for i in range(len(string)-1, -1, -1):
        c = string[len(string)-i-1]
        c_to_num = ord(c) - ord("a") + 1
        num += c_to_num * (26 ** i)
    return num