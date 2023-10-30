"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    lista = list(args);
    return lista


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    [a, b, c, *rest] = each_wagons_id
    lista = *missing_wagons, *rest
    lista = list(lista)
    locomotive = [c]
    endwagons = [a, b]
    lista = locomotive + lista + endwagons
    return lista


def add_missing_stops(orig_dest, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    lista = list(kwargs.values())
    stops = {'stops': lista}
    return {**orig_dest, **stops}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    l1, l2, l3 = wagons_rows

    l10a, l11b, l12c = l1
    l20a, l21b, l22c = l2
    l30a, l31b, l32c = l3

    lista = [[l10a, l20a, l30a],
             [l11b, l21b, l31b],
             [l12c, l22c, l32c]]
    return lista