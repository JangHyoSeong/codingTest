T = int(input())
for testcase in range(T):
    N = int(input())
    clothes_dict = {}

    type_set = set()
    for _ in range(N):
        name, clothes = input().split()
        type_set.add(clothes)
        if clothes_dict.get(clothes) is None:
            clothes_dict[clothes] = {name}
        else:
            clothes_dict[clothes].add(name)

    count = 1
    for type in type_set:
        count *= len(clothes_dict[type]) + 1
    
    print(count - 1)