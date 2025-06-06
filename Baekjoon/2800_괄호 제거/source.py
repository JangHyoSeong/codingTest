from itertools import combinations

string = input()

stack = []
pairs = []

for i, c in enumerate(string):
    if c == "(":
        stack.append(i)
    
    elif c == ")":
        start = stack.pop()
        pairs.append((start, i))
    
results = set()
for r in range(1, len(pairs) + 1):
    for combo in combinations(pairs, r):
        remove = set()
        for start, end in combo:
            remove.add(start)
            remove.add(end)
        
        new_string = "".join(
            string[i] for i in range(len(string)) if i not in remove
        )

        results.add(new_string)

for result in sorted(results):
    print(result)