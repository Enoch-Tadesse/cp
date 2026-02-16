length, change = list(map(int, input().split()))
word = input()
temp_c = change


def calculate(first, change):
    i = 0
    index = 0
    size = 0
    while i < len(word):
        if word[i] != first:
            if change:
                change -= 1
            else:
                while not change:
                    change += word[index] != first
                    index += 1

        i += 1
        size = max(size, i - index)
    return size


a = calculate("a", temp_c)
print(a)
# b = calculate("b", temp_c)
# print(max(a, b))
