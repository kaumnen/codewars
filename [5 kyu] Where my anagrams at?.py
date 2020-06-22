def anagrams(word, words):
    result = []
    temp = 0
    i = 0
    while i < len(words):
        if len(words[i]) == len(word):
            for j in range(len(word)):
                if words[i][j] in word and word[j] in words[i]:
                    temp += 1
                if temp == len(word):
                    result.append(words[i])
            temp = 0
        i += 1
    return result
