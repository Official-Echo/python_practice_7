import pandas as pd


def read_from_console():
    """
    Reads text input from the console provided by the user.

    Returns
    -------
    str
        The text entered by the user via the console.
    """
    return input("Enter text: ")


def read_from_file_builtin(file_name="data/sample.txt"):
    """
    Reads content from a text file using Python's built-in file handling.

    Parameters
    ----------
    file_name : str
        File handle that is going to be read from. Defaults to "data/sample.txt"

    Returns
    -------
    str
        The content of the file as a single string.
    """
    with open(file_name, "r") as file:
        return file.read()


def read_from_file_pandas(file_name="data/sample.csv"):
    """
    Reads content from a CSV file using the pandas library.

    Parameters
    ----------
    file_name : str
        File handle that is going to be read from. Defaults to "data/sample.txt"

    Returns
    -------
    str
        The content of the CSV file as a string representation of a pandas DataFrame.
    """
    df = pd.read_csv(file_name)
    return df.to_string()
