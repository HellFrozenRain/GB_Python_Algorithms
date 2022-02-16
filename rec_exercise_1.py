"""Write a function that reverses a string. The input string is given
as an array of characters"""


def array_reverse(array):
    if not array:
        return []
    return [array.pop()] + array_reverse(array)


string = ["h", "e", "l", "l", "o"]
print(array_reverse(string))

