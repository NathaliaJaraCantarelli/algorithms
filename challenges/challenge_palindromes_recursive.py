def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    word = word.lower()

    if word[low_index] != word[high_index]:
        return False

    if high_index <= low_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
