"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letras = ['A', 'B', 'C', 'D']

    index = 0
    loopctr = 1

    while loopctr <= number:

        yield letras[index]

        if index >= 3:
            index = 0
        else:
            index += 1

        loopctr += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    genletter = generate_seat_letters(number)

    index = 1
    whilectr = 1

    while whilectr <= number:
        letra = next(genletter)
        if index == 13:
            index = 14
        yield f'{index}{letra}'
        if letra == 'D':
            index += 1
        whilectr += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assigns = {}
    generador = generate_seats(200)

    for person in passengers:
        assigns[person] = next(generador)

    return assigns


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    zero = '0'

    for seat in seat_numbers:
        seat_len = len(seat)
        fligh_len_id = len(flight_id)
        factor = 12 - seat_len - fligh_len_id
        filler = zero * factor

        yield f'{seat}{flight_id}{filler}'