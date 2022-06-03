from typing import Iterator, List


class PostOffice:
    """A Post Office class. Allows users to message each other.
    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.
    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames: list):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender: str, recipient: str, message_body: str, urgent=False, title: str = '') -> int:
        """Send a message to a recipient.
        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :param title: The title of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = Message(self.message_id, message_body, sender, urgent, title)
        print(message_details)
        user_box.insert(0, message_details) if urgent else user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username: str, number_of_n_first_messages=0) -> Iterator[str]:
        """
        Get username and an optional parameter N for the first N messages to read from the inbox
        of the user. If the messages were not read yet, return the messages (the first N messages)
        if the messages were read already return nothing. If the N is not sent or it is bigger than
        the actual number of messages, return all messages in the inbox.
        :param username: The name of the user.
        :param number_of_n_first_messages: The number of messages to read from the first message.
        :return: An iterator of the body of the N first messages (or all the messages in the inbox).
        """
        max_messages = self.boxes[username][-1].id
        if not number_of_n_first_messages or number_of_n_first_messages > max_messages:
            number_of_n_first_messages = max_messages

        for i in range(0, number_of_n_first_messages):
            if not self.boxes[username][i].read:
                self.boxes[username][i].read = True
                yield self.boxes[username][i].body

    def search_inbox(self, username: str, substring: str) -> List[str]:
        """
        Get username and and a string, return list of message that contains the string sent.
        :param username: The name of the user.
        :param substring: A substring to check if exist in each message
        :return: A list of message that contains the string sent.
        """
        list_messages = [self.boxes[username][i].body for i in range(0, self.boxes[username][-1].id)]
        return list(filter(lambda message: substring in message, list_messages))


class Message:
    def __init__(self, m_id: int, body: str, sender: str, urgent=False, title: str = ''):
        self.id = m_id
        self.title = title
        self.body = body
        self.sender = sender
        self.urgent = urgent
        self.read = False

    def __repr__(self):
        return f"id: '{self.id}', title: '{self.title}', body: '{self.body}', sender: '{self.sender}'," \
               f" read: {self.read}, urgent: {self.urgent}"

    def __len__(self):
        return len(self.body)


def test_post_office():
    """Show example of using the PostOffice class."""

    # Change from tuple to list because PostOffice expect a list and not a tuple
    users = ['Newman', 'Mr. Peanutbutter']
    post_office = PostOffice(users)
    post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='Hello, Newman.', title='Start chat'
    )
    post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='Come quick!!! This is urgent!!!',
        urgent=True, title='Urgent!!!'
    )
    post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='How are you?',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='Hope you are feeling OK',
    )

    print(f"Successfully sent message number {message_id}.\n")
    print(post_office.boxes['Newman'])

    print("\nUnread messages:")
    print("*** first call (2 first messages):")
    for message in post_office.read_inbox('Newman', 2):
        print(message)
    print("*** second call (all (3) messages that are not read yet):")
    for message in post_office.read_inbox('Newman'):
        print(message)

    print("\nSearch in inbox messages containing 'you':")
    print(post_office.search_inbox('Newman', 'you'))


if __name__ == '__main__':
    test_post_office()

