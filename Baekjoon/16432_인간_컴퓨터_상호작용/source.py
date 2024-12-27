import sys

string = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline().rstrip())

len_string = len(string)
char_dict = {}
for num in range(ord('a'), ord('z')+1):
    char_dict[chr(num)] = [0] * (len_string + 1)

for i in range(1, len_string + 1):
    for num in range(ord('a'), ord('z')+1):
        char_dict[chr(num)][i] = char_dict[chr(num)][i-1]
    
    char_dict[string[i-1]][i] += 1

for _ in range(q):
    c, l, r = sys.stdin.readline().rstrip().split()
    print(char_dict[c][int(r)+1] - char_dict[c][int(l)])