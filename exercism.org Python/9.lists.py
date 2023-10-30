"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    qitems = len(hand)
    suma = sum(hand)
    return suma/qitems


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    promedio = card_average(hand)
    extremos = (hand[0] + hand[-1]) / 2
    median_index = len(hand) // 2
    if promedio in (extremos, hand[median_index]):
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    qitems = len(hand)
    items_odd = 0
    items_even = 0
    sum_odd = 0
    sum_even = 0
    index = 0
    while index <= qitems-1:
        sum_even += hand[index]
        items_even += 1
        index += 2
    ave_even = sum_even/items_even
    index = 1
    while index <= qitems-1:
        sum_odd += hand[index]
        items_odd += 1
        index += 2
    ave_odd =sum_odd/items_odd
    if ave_even == ave_odd:
        return True
    return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand