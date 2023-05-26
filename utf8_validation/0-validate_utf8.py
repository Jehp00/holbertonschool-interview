#!/usr/bin/python3
"""Valid UTF-8 data"""


def validUTF8(data):
    """
    :param data: number or list of number to check
    :return: True if is utf-8, otherwise false
    """
    NUMBER_OF_BITS_PER_BLOCK = 8
    MAX_NUMBER_OF_ONES = 4
    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
        if number == 0:
            index += 1
            continue
        number_of_ones = 0
        while True:
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (NUMBER_OF_BITS_PER_BLOCK - number_of_ones - 1)
            if number == 1:
                number_of_ones += 1
            else:
                break
            if number_of_ones > MAX_NUMBER_OF_ONES:
                return False
        if number_of_ones == 1:
            return False
        index += 1
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False

        for i in range(index, index + number_of_ones - 1):
            if data[i] > index:
                return False
            number = data[i]
            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 1:
                return False
            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 0:
                return False
            index += 1
    return True

"""if __name__ == '__main__':
    validUTF8 = __import__('0-validate_utf8').validUTF8

    data = [235, 140]
    print(validUTF8(data))
"""