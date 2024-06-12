T = int(input())

numbers = {
    
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010', 
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000'
}

for testcase in range(T):
    a, b = map(str, input().split())
    result = 0

    a_empty = 5 - len(a)
    b_empty = 5 - len(b)

    a = ' ' * a_empty + a
    b = ' ' * b_empty + b

    for i in range(5):
        for j in range(7):
            if numbers[a[i]][j] != numbers[b[i]][j]:
                result += 1

    print(result)