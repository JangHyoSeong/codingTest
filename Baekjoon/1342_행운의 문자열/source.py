from collections import Counter

S = input()
counter = Counter(S)
result = 0

path = []

stack = [(path, counter)]

while stack:
    current_path, current_counter = stack.pop()

    if len(current_path) == len(S):
        result += 1
        continue

    for char in current_counter:
        if current_counter[char] > 0:
            if current_path and current_path[-1] == char:
                continue
        
            next_path = current_path + [char]
            next_counter = current_counter.copy()
            next_counter[char] -= 1
            
            stack.append((next_path, next_counter))

print(result)