def find_anagrams(word, candidates):
    upper_cand = []
    word = word.upper()
    for item in candidates:
        upper_cand.append(item.upper())

    letters = list(word)
    letters.sort()
    result = []

    for index, item in enumerate(upper_cand):
        if len(item) == len(word) and item != word:
            each_lett = list(item)
            each_lett.sort()
            if each_lett == letters:
                result.append(candidates[index])

    return result