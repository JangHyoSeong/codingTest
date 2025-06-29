N = int(input())
M = int(input())
arr = list(map(int, input().split()))

frame = dict()

for t, student in enumerate(arr):
    if student in frame:
        frame[student][0] += 1
    else:
        if len(frame) == N:
            to_remove = min(frame.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            del frame[to_remove]
        frame[student] = [1, t]

print(' '.join(map(str, sorted(frame.keys()))))