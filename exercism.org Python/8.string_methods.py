"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    pref = vocab_words[0]
    result = pref + ' :: '
    long = len(vocab_words)
    for index in range(long - 1):
        result = result + pref + vocab_words[index + 1]
        if index != long - 2:
            result = result + ' :: '
    return result


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    long = len(word)
    new_word = word[:long - 4]
    l1 = len(new_word)
    if new_word[l1 - 1] == 'i':
        result = new_word[:l1 - 1] + 'y'
        return result
    return new_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    long = len(sentence)
    new_sentence = sentence[:long - 1]
    words = new_sentence.split()
    lw = len(words)
    if index < 0:
        index = index + lw
    return words[index] + 'en'