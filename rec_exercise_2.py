"""given an integer n, return true, if it is power of two.
otherwise, return false"""


def power_of_two(number):
    if number == 1:
        return True
    if number & 1:
        return False
    return power_of_two(number >> 1)


print(power_of_two(512))
print(power_of_two(513))
