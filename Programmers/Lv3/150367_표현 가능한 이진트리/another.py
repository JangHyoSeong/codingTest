from math import log2, ceil




def solution(numbers):

    def divide(bin_num, idx):
        
        length = len(bin_num)

        if length == 0:
            return
        
        root = length//2
        left_tree = bin_num[:root]
        right_tree= bin_num[root+1:]

        if bin_num[root] == '0':
            
            if '1' in bin_num:
                numbers[idx] = 0
        else:
            divide(left_tree, idx)
            divide(right_tree, idx)

    for idx, num in enumerate(numbers):

        numbers[idx] = 1
        bin_num = bin(num)[2:]
        bin_len = len(bin_num)
        L=1
        while bin_len >= L:
            L*=2
        height = ceil(log2(bin_len))
        temp = 2**height

        bin_num = bin_num.zfill(L-1)
        divide(bin_num, idx)

       
    return numbers