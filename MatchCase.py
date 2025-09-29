def get_number_explanation(status):
    match status:
        case 666:
            print('devil number')
        case 42:
            print('answer for everything')
        case 7:
            print('prime number')
        case _:
            print('just a number')