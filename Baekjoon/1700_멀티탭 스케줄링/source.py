N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
used = [False] * (K+1)
now = []

for i in range(K):
    if len(now) < N:
        if not used[arr[i]]:
            now.append(arr[i])
            used[arr[i]] = True

    else:
        if used[arr[i]]:
            continue
        
        last_used = -1
        device_to_unplug = -1
        for num in now:
            if num not in arr[i:]:
                device_to_unplug = num
                break
        
            else:
                next_use = arr[i:].index(num)
                if next_use > last_used:
                    last_used = next_use
                    device_to_unplug = num

        now.remove(device_to_unplug)
        now.append(arr[i])
        used[device_to_unplug] = False
        used[arr[i]] = True
        count += 1

print(count)