class IDIterator:
    """
    Iterator class to generate valid ID numbers starting from a given ID.

    Attributes:
        _id_ (int): The starting ID number.
        _current (int): The current ID number being checked.
    """

    def __init__(self, id):
        """
        Initialize the iterator with the starting ID.

        Args:
            id (int): The starting ID number.
        """
        self._id_ = id
        self._current = id

    def __iter__(self):
        """
        Return the iterator object.

        Returns:
            IDIterator: The iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next valid ID number in the sequence.

        Returns:
            int: The next valid ID number.

        Raises:
            StopIteration: If no valid ID numbers are left in the range.
        """
        self._current += 1
        while self._current <= 999999999:
            if check_id_valid(self._current):
                return self._current
            self._current += 1
        raise StopIteration


def check_id_valid(id_number):
    """
    Check if a given ID number is valid.

    Args:
        id_number (int): The ID number to be checked.

    Returns:
        bool: True if the ID number is valid, False otherwise.
    """
    doubled_digits = [int(digit) * (2 if i % 2 == 1 else 1) for i, digit in enumerate(str(id_number))]
    summed_digits = [sum(int(digit) for digit in str(num)) if num > 9 else num for num in doubled_digits]
    total = sum(summed_digits)
    return total % 10 == 0


def id_generator(start_id):
    """
    Generator to produce valid ID numbers starting from a given ID.

    Args:
        start_id (int): The ID number to start from.

    Yields:
        int: The next valid ID number.
    """
    current = start_id + 1
    while current <= 999999999:
        if check_id_valid(current):
            yield current
        current += 1


def main():
    """
    Main function to prompt the user for an ID number and a method (iterator or generator).

    Depending on the method chosen, generates and prints the next 10 valid ID numbers.
    """
    user_input = input("Enter ID: ")
    id_number = int(user_input)
    method = input("Enter 'it' for iterator or 'gen' for generator: ").strip().lower()

    if method == "it":
        iterator = IDIterator(id_number)
        for _ in range(10):
            print(next(iterator))
    elif method == "gen":
        generator = id_generator(id_number)
        for _ in range(10):
            print(next(generator))
    else:
        print("Invalid input, please enter 'it' or 'gen'.")


if __name__ == "__main__":
    main()
