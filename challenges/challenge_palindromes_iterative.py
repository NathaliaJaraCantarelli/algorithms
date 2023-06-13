def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    word = word.lower().replace(" ", "")
    reverse = word[::-1]
    is_palindrome = word == reverse
    return is_palindrome
