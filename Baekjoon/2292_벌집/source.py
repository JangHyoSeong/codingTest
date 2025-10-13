N = int(input())
layer = 1
num = 1

while N > num:
    num += 6 * layer
    layer += 1

print(layer)