from math import log2, ceil

def divide(bin_num):

    global flag
    if flag:
        return
    
    length = len(bin_num)
    if length == 0:
        return
    
    root = length//2
    left_tree = bin_num[:root]
    right_tree= bin_num[root+1:]

    if bin_num[root] == '0':

        if flag:
            return
        
        if '1' in bin_num:
            flag = True
            return
    else:
        divide(left_tree)
        divide(right_tree)


def solution(numbers):
    answer = []
    global flag

    for num in numbers:
        flag = False

        bin_num = bin(num)[2:]
        bin_len = len(bin_num)
        
        height = ceil(log2(bin_len))
        temp = 2**height

        bin_num = bin_num.zfill(temp-1)
        divide(bin_num)

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer