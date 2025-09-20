def has_upper_case(a):
    return any(char.isupper() for char in a)
print(has_upper_case('hello'))