from math import log2, ceil

def isvalid(bin_num, parent, length):

    global flag
    if flag:
        return
    
    left = parent - 1
    right = parent + 1

    if 0 <= left < length and 0 <= right < length:
        if bin_num[left] == '1' or bin_num[right] == '1':
            if bin_num[parent] == '0':
                flag = True
                return
            else:
                isvalid(bin_num, left, length)
                if not flag:
                    isvalid(bin_num, right, length)
    
    
    else:
        return



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
        root = (temp-1)//2

        isvalid(bin_num, root, temp-1)

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer



numbers = [7, 42, 5]
print(solution(numbers))