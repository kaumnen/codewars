import itertools
def permutations(string):
    
    result = []
    string_array = [x for x in string]
    possible_comb = itertools.permutations(string_array)
  
    for comb in possible_comb:
        result.append(''.join(comb))
    
    return list(set(result))
