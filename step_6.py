def cube(number):
    cube = number ** 3
    return cube


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
