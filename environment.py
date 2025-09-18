def get_age_difference(bday, nday):
    return f"The age difference is {abs(nday - bday)}"

actual = get_age_difference(2001, 2018)
print(actual)
