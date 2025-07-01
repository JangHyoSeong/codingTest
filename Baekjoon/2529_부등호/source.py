K = int(input())
arr = list(input().split())

max_answer = ''
min_answer = ''

visited = [False] * 10

def valid(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b

def backtrack(depth, result):
    global max_answer, min_answer

    if depth == K+1:
        if not min_answer:
            min_answer = result
        
        else:
            max_answer = result
        
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or valid(int(result[-1]), i, arr[depth - 1]):
                visited[i] = True
                backtrack(depth + 1, result + str(i))
                visited[i] = False
    
backtrack(0, '')
print(max_answer)
print(min_answer)