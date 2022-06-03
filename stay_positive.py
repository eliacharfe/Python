

def get_positive_numbers(my_input: str) -> list:
    """
    A function that gets an input of numbers seperated by ',' and return a list of the positive numbers
    :param my_input: The input from the user
    :return: list of all positives
    """
    return list(filter(lambda x: int(x) > 0, list(map(int, my_input.split(",")))))


if __name__ == '__main__':
    print(get_positive_numbers(input("Enter a serie of numbers separated by ',': \n")))

