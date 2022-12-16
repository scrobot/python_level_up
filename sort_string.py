def sort_words(string: str) -> str:
    return ' '.join(sorted(string.split(), key=str.casefold))

if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))
