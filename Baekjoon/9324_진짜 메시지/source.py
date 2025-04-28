import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    message = sys.stdin.readline().rstrip()
    count_char = [0] * 26

    i = 0
    while i < len(message):
        c = message[i]
        alphabet = ord(c) - ord("A")
        count_char[alphabet] += 1

        if count_char[alphabet] == 3:
            if i+1 < len(message):
                if message[i+1] != message[i]:
                    print("FAKE")
                    break
                else:
                    count_char[alphabet] = 0
                    i += 1
            else:   
                print("FAKE")
                break
        i += 1
    else:
        print("OK")