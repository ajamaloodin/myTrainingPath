def find(search_list, value):

    search_list.sort()
    cuantos = len(search_list)

    if cuantos == 1:
        if search_list[0] == value:
            return 0
        else:
            raise ValueError("value not in array")

    indices = []
    for indx in range(cuantos):
        indices.append(indx)

    count = 1
    while cuantos > 0:

        index = int(cuantos / 2)
        if search_list[index] > value:
            for i in range(cuantos-index):
                search_list.pop(-1)
                indices.pop(-1)
        else:
            if search_list[index] == value:
                return indices[index]
            for i in range(cuantos-index):
                search_list.pop(0)
                indices.pop(0)
        cuantos = len(search_list)
        count += 1
    raise ValueError("value not in array")