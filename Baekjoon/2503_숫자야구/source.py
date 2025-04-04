from itertools import permutations

N = int(input())

possible_numbers = list(permutations(range(1, 10), 3))

for _ in range(N):
    query, strike, ball = map(int, input().split())

    new_possible_numbers = []
    for num in possible_numbers:
        num = list(num)
        query_list = list(map(int, str(query)))

        s, b = 0, 0

        for i in range(3):
            if num[i] == query_list[i]:
                s += 1
            elif query_list[i] in num:
                b += 1

        if s == strike and b == ball:
            new_possible_numbers.append(num)
    
    possible_numbers = new_possible_numbers

print(len(possible_numbers))
