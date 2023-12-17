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


def resistor_label(colors):
    tolerance = {'grey': ' ±0.05%', 'violet': ' ±0.1%', 'blue': ' ±0.25%', 'green': ' ±0.5%', 'brown': ' ±1%',
                 'red': ' ±2%', 'gold': ' ±5%', 'silver': ' ±10%'}
    tolerance_value = ''
    long_col = len(colors)
    if long_col > 1:
        if long_col == 4:
            value = str((COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * 10**COLORS.index(colors[2]))
            tolerance_value = tolerance[colors[3]]
        else:
            value = str( (COLORS.index(colors[0]) * 100 + COLORS.index(colors[1]) * 10 +
                         COLORS.index(colors[2])) * 10 ** COLORS.index(colors[3]) )
            tolerance_value = tolerance[colors[4]]
    else:
        value = str(COLORS.index(colors[0]))

    num_of_zeros = value.count('0')
    long = len(value)

    if num_of_zeros >= 3 and num_of_zeros <= 5:
        if int(value[:long-3]) < 1000:
            return value[:long-3] + ' kiloohms' + tolerance_value
        return str(int(value[:long-3])/1000) + ' megaohms' + tolerance_value
    if num_of_zeros >= 6 and num_of_zeros <= 8:
        if int(value[:long - 6]) < 1000:
            return value[:long - 6] + ' megaohms' + tolerance_value
        return str(int(value[:long - 6]) / 1000) + ' gigaohms' + tolerance_value
    if num_of_zeros == 9:
        return value[:long - 9] + ' gigaohms' + tolerance_value

    if int(value) < 1000:
        return value + ' ' + 'ohms' + tolerance_value
    return str(int(value)/1000) + ' ' + 'kiloohms' + tolerance_value



