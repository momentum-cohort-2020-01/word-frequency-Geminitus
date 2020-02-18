import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        lines = ' '.join(file.readlines())
        print(lines)
        l_words = lines.lower()
        words = l_words.split(' ')
        just_words = [s.translate(string.punctuation) for s in words]
        word_count = {}
        for word in just_words:
            x = l_words.count(word)
            y = word
            # if y in word_count == False:
            word_count[word] = x + 1
        print(word_count.items())


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
