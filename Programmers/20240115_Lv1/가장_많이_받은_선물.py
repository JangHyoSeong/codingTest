def solution(friends, gifts):
    answer = 0
    COLUM = len(friends)
    ROW = len(friends)
    board = [[0 for i in range(COLUM)] for j in range(ROW)] 
    arr = [0 for i in range(COLUM)]
    giftScore = [0 for i in range(COLUM)]
    
    for i in range(len(gifts)):
        give, take = gifts[i].split()
        giveFlag = 0
        takeFlag = 0
        
        for j in range(len(friends)):
            if give == friends[j]:
                giveFlag = j
                giftScore[j] += 1
            if take == friends[j]:
                takeFlag = j
                giftScore[j] -= 1
                
        board[giveFlag][takeFlag] += 1
        

    for i in range(COLUM):
        for j in range(ROW):
            if board[i][j] > board[j][i]:
                arr[i] += 1
            elif board[i][j] == board[j][i]:
                if giftScore[i] > giftScore[j]:
                    arr[i] += 0.5
                elif giftScore[i] < giftScore[j]:
                    arr[j] += 0.5

    answer = max(arr)
                
            
    return answer