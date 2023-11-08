def convert(number):
    factor = [3,5,7]
    drops = ['Pling', 'Plang', 'Plong']

    result = ''
    for index in range(3):
        if number % factor[index] == 0:
            result = result + drops[index]
    if len(result) > 0:
        return result
    else:
        return str(number)