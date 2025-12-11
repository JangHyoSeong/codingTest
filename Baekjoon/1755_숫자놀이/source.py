M, N = map(int, input().split())

num_to_word = {
    '0': "zero", '1': "one", '2': "two", '3': "three", '4': "four",
    '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"
}

arr = []

for num in range(M, N + 1):
    word = " ".join(num_to_word[d] for d in str(num))
    arr.append((word, num))

arr.sort(key=lambda x : x[0])
for i in range(len(arr)):
    print(arr[i][1], end=" ")
    if (i + 1) % 10 == 0:
        print()