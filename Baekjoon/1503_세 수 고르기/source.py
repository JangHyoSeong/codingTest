N, M = map(int, input().split())
S = list(map(int, input().split())) if M > 0 else []

all_numbers = set(range(1, 1002))
valid_numbers = sorted(all_numbers - set(S))

min_diff = 21e8

for x in valid_numbers:
    for y in valid_numbers:
        for z in valid_numbers:
            min_diff = min(min_diff, abs(N-x*y*z))

print(min_diff)