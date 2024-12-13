N = int(input())
genoms = input().split()

phenotypes = set()

for x in range(ord('A'), ord('Z') + 1):
    x_char = chr(x)
    count = 0

    for genom in genoms:
        if genom[0] == x_char:
            count += 1

    if count > 1:
        for genom in genoms:
            phenotypes.add(max(x_char, genom[1]))
    elif count == 1:
        for genom in genoms:
            if genom[0] != x_char:
                phenotypes.add(max(x_char, genom[1]))

sorted_phenotypes = sorted(phenotypes)

print(len(sorted_phenotypes))
print(" ".join(sorted_phenotypes))
