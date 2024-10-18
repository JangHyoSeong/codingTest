def solution(queue1, queue2):
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    queue_sum = queue1_sum + queue2_sum
    
    if queue_sum%2:
        return -1
    
    target = queue_sum // 2
    if queue1_sum == target:
        return 0
    
    answer = 0
    idx1, idx2 = 0, 0
    
    while True:
        if idx1 >= len(queue1) or idx2 >= len(queue2):
            return -1
        
        if queue1_sum == target:
            return answer
        
        if queue1_sum > target:
            queue1_sum -= queue1[idx1]
            idx1 += 1
        else:
            queue1_sum += queue2[idx2]
            queue1.append(queue2[idx2])
            idx2 += 1
            
        answer += 1