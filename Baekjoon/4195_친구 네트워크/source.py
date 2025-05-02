import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]

    return size[x_root]

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    F = int(sys.stdin.readline().rstrip())
    parent = {}
    size = {}
    name_to_id = {}
    id_counter = 0

    for _ in range(F):
        a, b = sys.stdin.readline().rstrip().split()
        for person in [a, b]:
            if person not in name_to_id:
                name_to_id[person] = id_counter
                parent[id_counter] = id_counter
                size[id_counter] = 1
                id_counter += 1

        a_id = name_to_id[a]
        b_id = name_to_id[b]
        print(union(a_id, b_id))
