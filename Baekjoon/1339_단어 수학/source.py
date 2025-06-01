N = int(input())
words = [input() for _ in range(N)]

weight = {}
for word in words:
    power = len(word) - 1

    for char in word:
        if char in weight:
            weight[char] += 10 ** power
        else:
            weight[char] = 10 ** power
        
        power -= 1
    
sorted_weight = sorted(weight.items(), key=lambda x : x[1], reverse=True)
num = 9
char_to_digit = {}
for char, _ in sorted_weight:
    char_to_digit[char] = num
    num -= 1

total = 0
for word in words:
    number = ''
    for char in word:
        number += str(char_to_digit[char])
    total += int(number)

print(total)