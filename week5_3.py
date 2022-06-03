# לחששנית
import re


def open_binary_file(path):
    return open(path, "rb")


def find_all_hidden_messages_in_a_binary_file_via_pattern(path, pattern):
    """
    The function gets a path to a binary file, and a binary pattern and search all "strings" that
    matches the pattern (those are coded messages in the file) then returns a list of those messages
    as regular strings.
    :return: A list of the hidden messages
    """
    reg = re.compile(pattern)
    encrypted_binary_file = open_binary_file(path)

    lst_hidden_messages = [hidden_msg.decode('ascii') for line in encrypted_binary_file.readlines()
                           if reg.findall(line) for hidden_msg in reg.findall(line)]
    encrypted_binary_file.close()
    return ["".join(msg) for msg in lst_hidden_messages]


if __name__ == '__main__':
    print('\n'.join(
        find_all_hidden_messages_in_a_binary_file_via_pattern("resources/logo.jpg", b'[a-z]{5,}!')))