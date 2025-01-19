from collections import Counter

N = int(input())
files = [input() for _ in range(N)]
ext_counts = Counter(f.split('.')[1] for f in files)  # 확장자 개수 세기

for ext in sorted(ext_counts):
    print(ext, ext_counts[ext])