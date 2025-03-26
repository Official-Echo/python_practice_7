from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import print_to_console, write_to_file_builtin


def main():
    """
    Main function to demonstrate input and output operations.

    Returns
    -------
    None
    """
    # Read from different sources
    console_text = read_from_console()
    builtin_text = read_from_file_builtin()
    pandas_text = read_from_file_pandas()

    # Output to console
    print_to_console(console_text)
    print_to_console(builtin_text)
    print_to_console(pandas_text)

    # Write console input to file
    write_to_file_builtin(console_text)


if __name__ == "__main__":
    main()
