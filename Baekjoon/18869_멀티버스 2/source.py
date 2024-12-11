from collections import defaultdict

def count_uniform_universes(M, N, universes):
    # 좌표 압축을 통해 각 우주의 순위 배열을 계산
    def compress(universe):
        sorted_uni = sorted(set(universe))
        rank_map = {value: rank for rank, value in enumerate(sorted_uni)}
        return tuple(rank_map[value] for value in universe)

    # 모든 우주를 압축된 순위 배열로 변환
    compressed_universes = [compress(universe) for universe in universes]

    # 순위 배열을 카운팅하여 균등한 쌍 계산
    freq = defaultdict(int)
    for compressed in compressed_universes:
        freq[compressed] += 1

    # 같은 순위 배열이 나타난 횟수로 균등한 쌍의 개수를 계산
    result = 0
    for count in freq.values():
        if count > 1:
            result += count * (count - 1) // 2  # 조합 계산

    return result

# 입력 처리
M, N = map(int, input().split())
universes = [list(map(int, input().split())) for _ in range(M)]

# 균등한 우주의 쌍 계산
result = count_uniform_universes(M, N, universes)
print(result)
