import re
import collections

def _download_file(url, filename):
    # download text file from the url and put it in the current directory with filename
    import requests
    with open(filename, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)

def count_words(path):
    # TODO wrap this in a try/except block to catch errors
    filename = path.split('/')[-1]
    _download_file(path, filename)

    with open(filename, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')

if __name__ == '__main__':
    count_words('https://www.gutenberg.org/files/1661/1661-0.txt')