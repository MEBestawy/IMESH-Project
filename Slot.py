class Slot:
    """

    """

    def __init__(self, disc=None):
        """
        Constructor for a slot object

        :param disc: The disc that the slot contains.
        """
        self.disc = disc

    def place(self, disc):
        """

        :param disc:
        :return:
        """
        # Checking if the slot is empty and inserting disk
        if self.is_empty():
            self.disc = disc
            return True
        # This slot is already full.
        return False

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
        return str(self.disc)

