def make_readable(seconds):
    #hh : 3600, mm: 60
    if seconds // 3600 < 1:
        if seconds // 60 < 1:
            return f'00:00:{seconds:02d}'
        else:
            Minute = seconds // 60
            seconds = seconds % 60
            return f'00:{Minute:02d}:{seconds:02d}'
    else:
        Hour = seconds // 3600
        seconds = seconds % 3600
        Minute = seconds // 60
        seconds = seconds % 60
        return f'{Hour:02d}:{Minute:02d}:{seconds:02d}'
