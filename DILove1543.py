t = int(input())


def spiral(mat):
    return mat and [*mat.pop(0)] + spiral([*zip(*mat)][::-1])


for _ in range(t):
    r, c = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(r)]
    print(mat)
    out = spiral(mat)
    # out = [out[-2], out[-1]] + out + [out[0], out[1]]
    counter = 0
    for i in range(-3, len(out) + 3):
        i %= r * c
        if out[i] == 1 and out[i + 1] == 5 and out[i + 2] == 4 and out[i + 3] == 3:
            counter += 1

    print(counter)
