import functools

def task1_longest():
    """
    Find the longest name in the file 'names.txt'.

    Returns:
        str: The longest name found in the file.
    """
    with open("names.txt", 'r') as file:
        return functools.reduce(lambda x, y: x if len(x) > len(y) else y, file.readlines())

def task2_sum():
    """
    Calculate the sum of the lengths of all names in the file 'names.txt'.

    Returns:
        int: The total sum of the lengths of all names.
    """
    with open("names.txt", 'r') as file:
        return functools.reduce(lambda x, y: x + len(y.strip()), file.readlines(), 0)

def task3_shortest():
    """
    Find and print the shortest name(s) in the file 'names.txt'.

    Prints:
        The shortest name(s) found in the file.
    """
    with open("names.txt", 'r') as file:
        names = file.readlines()
        mini = functools.reduce(lambda x, y: x if len(y.strip()) > len(x.strip()) else y, names).strip()
        print(*[name.strip() for name in names if len(name.strip()) == len(mini)], sep='\n')

def task4_len():
    """
    Write the length of each name in the file 'names.txt' to a new file 'name_length.txt'.

    Returns:
        None
    """
    with open("names.txt", 'r') as input_file, open("name_length.txt", 'w') as output_file:
        for name in input_file:
            output_file.write(str(len(name.strip())) + '\n')

def task5_in():
    """
    Prompt the user to enter a length and print all names in 'names.txt' with that length.

    Returns:
        None
    """
    length = int(input("Please enter length: "))
    [print(name.strip()) for name in open("names.txt").readlines() if len(name.strip()) == length]

def main():
    """
    Main function to execute all tasks.

    Returns:
        None
    """
    print(task1_longest())
    print(task2_sum())
    task3_shortest()
    task4_len()
    task5_in()

if __name__ == '__main__':
    main()
