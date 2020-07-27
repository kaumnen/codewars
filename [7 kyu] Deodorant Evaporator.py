def evaporator(content, evap_per_day, threshold):
    result = 0
    threshold_ml = (threshold / 100) * content
    while content > threshold_ml:
        content -= (evap_per_day / 100) * content
        result += 1
    return result
