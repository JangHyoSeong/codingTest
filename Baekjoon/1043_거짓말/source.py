N, M = map(int, input().split())
truth_num, *truth = map(int, input().split())

parties = [list(map(int, input().split())) for _ in range(M)]

representive = [i for i in range(N+1)]

def find_set(x):
    if representive[x] == x:
        return x

    return find_set(representive[x])

def union(x, y):

    x = find_set(x)
    y = find_set(y)
    

    if x != y:
        if y in truth:
            representive[x] = y
        else:
            representive[y] = x

    return

for party in parties:
    party_people = party[0]

    for i in range(1, party_people):
        union(party[i], party[i+1])

result = 0

for party in parties:
    party_people = party[0]
    for i in range(1, party_people+1):
        if find_set(party[i]) in truth:
            break
    else:
        result += 1

print(result)