import sys

def common_prefix_length(s1, s2):
    length = min(len(s1), len(s2))
    for i in range(length):
        if s1[i] != s2[i]:
            return i
    return length

N = int(sys.stdin.readline().strip())
words = [(sys.stdin.readline().strip(), i) for i in range(N)]

max_similarity = -1
best_pair = None

for i in range(N - 1):
    for j in range(i + 1, N):
        s1, idx1 = words[i]
        s2, idx2 = words[j]
        similarity = common_prefix_length(s1, s2)

        if similarity > max_similarity:
            max_similarity = similarity
            best_pair = (s1, s2, idx1, idx2)

        elif similarity == max_similarity:
            if idx1 < best_pair[2] or (idx1 == best_pair[2] and idx2 < best_pair[3]):
                best_pair = (s1, s2, idx1, idx2)

print(best_pair[0])
print(best_pair[1])