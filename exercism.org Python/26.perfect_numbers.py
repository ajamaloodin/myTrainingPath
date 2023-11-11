def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    lista = []
    for index in range(number-1):
        if number % (index+1) == 0:
            lista.append(index+1)
    test = sum(lista)
    if test == number:
        return "perfect"
    if test > number:
        return "abundant"
    return "deficient"
