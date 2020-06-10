import math
def find_next_square(sq):
    
    return (math.sqrt(sq) + 1) ** 2 if math.floor(math.sqrt(sq)) == math.sqrt(sq) else -1
