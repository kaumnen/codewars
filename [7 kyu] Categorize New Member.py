def openOrSenior(data):
    return ['Senior' if x[0] >= 55 and x[1] > 7 else 'Open' for x in data]
