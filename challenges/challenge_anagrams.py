def merge(left, right):
    result = ''
    arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])

    return result.join(arr)


def order(string):
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = order(string[:middle])
    right = order(string[middle:])

    return merge(left, right)


def is_anagram(first_string, second_string):
    first = order(first_string.lower())
    second = order(second_string.lower())

    if len(first) == 0 or len(second) == 0 or first != second:
        return (first, second, False)

    else:
        return (first, second, True)
