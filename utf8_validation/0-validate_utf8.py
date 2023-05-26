#!/usr/bin/python3
"""Valid UTF-8 data"""


def validUTF8(data):
    """
    :param data: number or list of number to check
    :return: True if is utf-8, otherwise false
    """
    num_bytes = 0

    for byte in data:
        # Check if the most significant bit (MSB) is set
        if num_bytes == 0:
            # Count the number of leading ones in the byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # A single byte character
            if num_bytes == 0:
                continue

            # Invalid UTF-8 character
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if byte >> 6 != 0b10:
                return False

        # Decrement the number of remaining bytes to process
        num_bytes -= 1
    return num_bytes == 0

"""if __name__ == '__main__':
    validUTF8 = __import__('0-validate_utf8').validUTF8

    data = [235, 140]
    print(validUTF8(data))
"""
