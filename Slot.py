class Slot:
    """

    """

    def __init__(self, disc=None):
        """

        :param disc:
        """
        self.disc = disc

    def is_empty(self):
        """
        :return: Whether the slot is empty.
        """
        return self.disc is None

    def __str__(self):
        """
        :return: The string representation of a slot on the connect 4 board.
        """
        # Return depending on if the slot is empty.
        if self.is_empty():
            return " "
        return "" + self.disc

