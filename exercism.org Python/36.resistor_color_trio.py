COLORS = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]


def label(colors):
    value = str((COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * 10**COLORS.index(colors[2]))
    num_of_zeros = value.count('0')
    long = len(value)

    if num_of_zeros >= 3 and num_of_zeros <= 5:
        return value[:long-3] + ' kiloohms'
    if num_of_zeros >= 6 and num_of_zeros <= 8:
        return value[:long - 6] + ' megaohms'
    if num_of_zeros == 9:
        return value[:long - 9] + ' gigaohms'
    return value + ' ' + 'ohms'