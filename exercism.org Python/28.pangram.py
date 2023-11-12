def is_pangram(sentence):
    check = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentence = sentence.upper()
    count = 0
    if len(sentence) >= 26:
        for index in range(26):
            if sentence.find(check[index]) != -1:
                count += 1
        if count == 26:
            return True
    return False
