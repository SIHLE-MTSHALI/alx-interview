#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list of int): A list of integers where each integer represents 1 byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7
    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits of the number
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            while byte & mask1:
                n_bytes += 1
                byte <<= 1

            # 1-byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # All characters should be complete
    return n_bytes == 0


if __name__ == "__main__":
    # Test cases
    print(validUTF8([65]))  # True
    print(validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]))  # True
    print(validUTF8([229, 65, 127, 256]))  # False
