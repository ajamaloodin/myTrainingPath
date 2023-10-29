"""Functions to keep track and alter inventory."""
import collections


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    invent = collections.Counter()
    for item in items:
        invent[item] += 1
    return dict(invent)


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    items.sort()
    nuevos = create_inventory(items)
    for key, value in nuevos.items():
        if inventory.get(key, 'nei') == 'nei':
            inventory[key] = value
        else:
            inventory[key] = inventory[key] + value
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    items.sort()
    nuevos = create_inventory(items)

    for key, value in nuevos.items():
        if inventory.get(key, 'nei') != 'nei':
            new_value = inventory[key] - value
            if new_value < 0:
                new_value = 0
            inventory[key] = new_value

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, 'not_there')
    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    lista = []
    latupla = tuple()
    for key, value in inventory.items():
        if value != 0:
            latupla = (key, value)
            lista.append(latupla)
    return lista
