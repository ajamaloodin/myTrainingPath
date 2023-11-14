def rotate(text, key):
    if key == 0 or key == 26:
        return text

    plain = 'abcdefghijklmnopqrstuvwxyz'
    sep = plain[key]

    lista = plain.split(sep)
    cipher = sep + lista[1] + lista[0]

    mytable = str.maketrans(plain, cipher)

    text2 = text.translate(mytable)

    plain = plain.upper()
    cipher = cipher.upper()

    mytable2 = str.maketrans(plain, cipher)

    return(text2.translate(mytable2))