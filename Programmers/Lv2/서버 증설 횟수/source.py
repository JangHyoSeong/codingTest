def solution(players, m, k):
    total_count = 0
    server_start = [0] * 24
    
    for i in range(24):
        player = players[i]
        need_server = player // m
        
        if i >= k:
            already_have = sum(server_start[i-k+1:i])

        else:
            already_have = sum(server_start[:i])
        
        
        if already_have < need_server:
            server_add = need_server - already_have
            total_count += server_add
            server_start[i] = server_add
            

    return total_count