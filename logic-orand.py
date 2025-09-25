def string_or_not(ornot):
    if isinstance(ornot, str):
        return 'yes'
    else:
        return 'no'
string_or_not('')