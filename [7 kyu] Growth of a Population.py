def nb_year(p0, percent, aug, p):
    counter = 0
    while p0 < p:
        p0 += p0 / 100 * percent + aug
        counter += 1
    return counter
