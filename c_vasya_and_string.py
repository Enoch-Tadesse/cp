length, change = list(map(int, input().split()))
word = input()
temp_c = change


def calculate(good, change):
    size = 0

    left = 0
    right = 0

    while right < len(word):
        # this is a bad character
        if word[right] != good:
            # if you have a change to use, use it
            if change > 0:
                change -= 1
            # change = 0, there is nothing to use,
            # so you should remove the leftmost
            # bad character
            else:
                # iterate as long as your left pointer is good
                while word[left] == good:
                    left += 1
                # this line is to skip the leftmost bad pointer
                left += 1
        # right - left + 1, is the size of your current window
        size = max(size, right - left + 1)
        right += 1
    return size


a = calculate("a", temp_c)
b = calculate("b", temp_c)
print(max(a, b))
