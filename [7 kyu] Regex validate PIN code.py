def validate_pin(pin):
    temp = [x for x in pin if x in '0123456789']
    return len(temp) == len(pin) if len(pin) in [4, 6] else False
