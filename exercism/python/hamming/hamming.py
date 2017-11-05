def distance(strand_a, strand_b):
    different = int(0)
    if len(strand_a) == len(strand_b):
        for i, letter in enumerate(strand_a):
            if letter != strand_b[i]:
                different += 1
            else:
                continue
    elif len(strand_a) < len(strand_b) or len(strand_a) > len(strand_b):
        raise ValueError('Second strand is longer than the first.')

    return different


