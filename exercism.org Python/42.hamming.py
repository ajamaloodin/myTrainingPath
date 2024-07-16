def distance(strand_a, strand_b):
    amany = len(strand_a)
    bmany = len(strand_b)

    if amany != bmany:
        raise ValueError("Strands must be of equal length.")

    if amany == 0 and bmany == 0:
        return 0

    if strand_a == strand_b:
        return 0

    count = 0
    for i in range(amany):
        if strand_a[i] != strand_b[i]:
            count += 1
    return count

