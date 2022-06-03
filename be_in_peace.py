from typing import Text, List


def words_length(sentence: [Text, str]) -> List[int]:
    """
    Function that gets a sentence of words and returns a list of the length of the words in it.
    :param sentence: The sentence.
    :return: A list of the lengths of the words in the sentence sent.
    """
    return [len(word) for word in sentence.split()]


if __name__ == '__main__':
    print("The list of the words length: "
          + str(words_length("Toto, I've a feeling we're not in Kansas anymore")))

