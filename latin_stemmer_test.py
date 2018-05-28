import latin_stemmer
import re


def stemmize_test():
    with open('latin_words.txt') as latin_words:
        for line in latin_words:
            print(line.strip())
            latin_word, latin_stem = re.split('\s+', line)[:2]
            latin_word_stemmized = latin_stemmer.stemmize(latin_word)
            assert latin_word_stemmized.stem == latin_stem


latin_stemmer.stemmize('cibus')
stemmize_test()
