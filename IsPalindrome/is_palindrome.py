import re


def is_palindrome(s):
    clean_sentence = re.sub(r'[\W_]', '', s).lower()
    i = 0
    j = len(clean_sentence) - 1

    while i < j:
        if clean_sentence[i] != clean_sentence[j]:
            return False
        i += 1
        j -= 1

    return True


print(is_palindrome("0P"))
