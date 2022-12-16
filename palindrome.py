def is_palindrome(source: str) -> bool:
    prepared = source.translate(str.maketrans('', '', '!@#$’,. -_')).lower()
    # reverse the string
    reversed = prepared[::-1]

    return prepared == reversed



if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome('hello world'))
    print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))