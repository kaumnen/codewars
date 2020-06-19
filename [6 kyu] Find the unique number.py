def find_uniq(arr):
    arr = sorted(arr)
    if arr[:3].count(arr[0]) > 1:
        return arr[-1]
    else:
        return arr[0]
