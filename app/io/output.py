def print_to_console(text):
    """
    Prints the provided text to the console.

    Parameters
    ----------
    text : str
        The text to be printed to the console.
    """
    print(text)


def write_to_file_builtin(text, file_name="data/output.txt"):
    """
        Writes the provided text to a file using Python's built-in file handling.

        Parameters
        ----------
        text : str
            The text to be written to the file.
        file_name : str
            File handle of the file to write to. Defaults to "data/output.txt"
        """
    with open("data/output.txt", "w") as file:
        file.write(text)
