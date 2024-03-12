move = [(1, 0), (0, -1), (0, 1), (-1, 0)]
dir = ['d', 'l', 'r', 'u']
flag = False


def maze(now_x, now_y, end_x, end_y, n, m, result, count, k):

    global flag
    global answer
    
    if flag:
        return None

    if count == k:
        if now_x == end_x and now_y == end_y:
            flag = True
            answer = result
            return result
        else:
            return None
    
    if abs(now_x - end_x) + abs(now_y - end_y) > k - count:
        return None
    
        
    for i in range(4):
        new_x = now_x + move[i][0]
        new_y = now_y + move[i][1]
        if 0 < new_x <= n and 0 < new_y <= m:
            if abs(new_x - end_x) + abs(new_y - end_y) + count + 1 <= k:
                maze(new_x, new_y, end_x, end_y, n, m, result + dir[i], count+1, k)


def solution(n, m, x, y, r, c, k):

    global answer
    answer = ''
    if (abs(r-x) + abs(c-y))%2 != k%2:
        return 'impossible'

    maze(x, y, r, c, n, m, '', 0, k)

    if answer == '':
        return 'impossible'

    return answer