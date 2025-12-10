target = input()
target_len = len(target)
N = int(input())

count = 0
for _ in range(N):
    ring = input()
    ring = ring + ring

    for i in range(20 - target_len):
        if target == ring[i:i+target_len]:
            count += 1
            break

print(count)