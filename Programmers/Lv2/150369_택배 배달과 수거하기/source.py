def solution(cap, n, deliveries, pickups):
    answer = 0

    last = n-1
    go_last = last
    come_last = last

    if deliveries.count(0) == n and pickups.count(0) == n:
        return 0

    while last >= 0:

        last = max(go_last, come_last)
        go = cap
        come = cap
        answer += 2 * (last + 1)


        while deliveries[go_last] < go and go_last >= 0:
            go -= deliveries[go_last]
            deliveries[go_last] = 0
            go_last -= 1

        if deliveries[go_last] > go and go_last >= 0:
            deliveries[go_last] -= go
            go = 0

        while deliveries[go_last] == go and go_last >= 0:
            deliveries[go_last] = 0
            go = 0
            go_last -= 1

        while pickups[come_last] < come and come_last >= 0:
            come -= pickups[come_last]
            pickups[come_last] = 0
            come_last -= 1

        if pickups[come_last] > come and come_last >= 0:
            pickups[come_last] -= come
            come = 0

        while pickups[come_last] == come and come_last >= 0:
            pickups[come_last] = 0
            come = 0
            come_last -= 1

    return answer