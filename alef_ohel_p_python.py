from typing import List


def get_letters() -> List[str]:
    """
    A function that returns a list of all lowercase and uppercase letters.
    :return: A list of all lowercase and uppercase letters.
    """
    return [chr(letter_low) for letter_low in range(ord('a'), ord('z') + 1)] + \
           [chr(letter_up) for letter_up in range(ord('A'), ord('Z') + 1)]


if __name__ == '__main__':
    print(get_letters())

