def response(hey_bob):
    hey_bob = hey_bob.strip(' ')
    if hey_bob.isupper() and hey_bob[-1] == '?':
        return "Calm down, I know what I'm doing!"
    if len(hey_bob) == 0 or hey_bob.isspace():
        return "Fine. Be that way!"
    if hey_bob[-1] == '?' or hey_bob[-2] == '?':
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"

    return "Whatever."