import re


def is_palindrome(s):
    clean_sentence = re.sub(r'[\W_]', '', s).lower()
    return clean_sentence == clean_sentence[::-1]


print(is_palindrome("0P"))
