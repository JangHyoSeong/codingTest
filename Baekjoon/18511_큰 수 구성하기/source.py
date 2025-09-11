N, k = map(int, input().split())
digits = list(map(int, input().split()))
digits.sort(reverse=True)

answer = 0

def dfs(s):
    global answer

    if s:
        num = int(s)
        if num <= N:
            answer = max(answer, num)
        else:
            return
        
    if len(s) >= len(str(N)):
        return
    
    for d in digits:
        dfs(s + str(d))

dfs("")
print(answer)