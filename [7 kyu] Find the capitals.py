def capitals(word):
    return sorted([x for x in range(len(word)) if word[x].isupper()])
