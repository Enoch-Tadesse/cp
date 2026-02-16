def helper(word, flag):
    first = "BA" if flag == True else "AB"
    second = "AB" if flag == True else "BA"

    index = word.find(first)

    if index == -1:
        return False
    left = word[:index]
    right = word[index + 2 :]

    if left.find(second) != -1:
        return True
    if right.find(second) != -1:
        return True
    return False


def solve():
    word = input().strip()

    can = helper(word, True) or helper(word, False)
    print("YES" if can else "NO")


solve()
