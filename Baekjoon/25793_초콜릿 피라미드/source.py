testcase = int(input())
black_answer = []
white_answer = []

for case in range(testcase):
    r, c = map(int,input().split())
    m, n = max(r, c), min(r, c)
    k = m - n
    white = n*(n+1)*(2*n+1)//3 - n*(n+1) + n*(n+1)*k - n*k + n
    black = n*(n+1)*(2*n+1)//3 - n*(n+1) + n*(n+1)*k - n*k
    white_answer.append(white)
    black_answer.append(black)

for i in range(testcase):
    print(f'{white_answer[i]} {black_answer[i]}')