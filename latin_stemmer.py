que_exceptions = {
    "atque", "quoque", "neque", "itaque", "absque", "apsque", "abusque", "adaeque", "adusque",
    "denique", "deque", "susque", "oblique", "peraeque", "plenisque", "quandoque", "quisque",
    "quaeque", "cuiusque", "cuique", "quemque", "quamque", "quaque", "quique", "quorumque",
    "quarumque", "quibusque", "quosque", "quasque", "quotusquisque", "quousque", "ubique",
    "undique", "usque", "uterque", "utique", "utroque", "utribique", "torque", "coque",
    "concoque", "contorque", "detorque", "decoque", "excoque", "extorque", "obtorque", "optorque",
    "retorque", "recoque", "attorque", "incoque", "intorque", "praetorque"
}

noun_suffixes = [
    "ibus", "ius",
    "ae", "am", "as", "em", "es", "ia", "is", "nt", "os", "ud", "um", "us",
    "a", "e", "i", "o", "u"
]


class Word:
    def __init__(self, stem, suffix):
        self.stem = stem
        self.suffix = suffix


def stemmize(word):
    word = word.replace('j', 'i').replace('v', 'u')

    if word.endswith('que'):
        if word in que_exceptions:
            return Word(stem=word, suffix='')
        word = word[:-3]

    for noun_suffix in noun_suffixes:
        if word.endswith(noun_suffix):
            if len(word) - len(noun_suffix) >= 2:
                return Word(stem=word[:-len(noun_suffix)], suffix=noun_suffix)
            else:
                return Word(stem=word, suffix='')

    return Word(stem=word, suffix='')
