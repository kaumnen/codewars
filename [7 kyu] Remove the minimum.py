def remove_smallest(numbers):
    result = []
    result += numbers
    if result == []:
        return []
    result.remove(min(numbers))
    return result
