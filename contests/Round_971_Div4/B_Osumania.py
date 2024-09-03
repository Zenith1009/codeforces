def osu(beatmap):
    result = []
    for row in reversed(beatmap):
        for i, char in enumerate(row, 1):
            if char == '#':
                result.append(str(i))
                break
    return ' '.join(result)

t = int(input())

for _ in range(t):
    n = int(input())
    beatmap = [input().strip() for _ in range(n)]
    print(osu(beatmap))