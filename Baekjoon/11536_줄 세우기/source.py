N = int(input())
names = [input() for _ in range(N)]

names_asc = sorted(names)
names_desc = sorted(names, reverse=True)

if names == names_asc:
    print('INCREASING')
elif names == names_desc:
    print('DECREASING')
else:
    print('NEITHER')