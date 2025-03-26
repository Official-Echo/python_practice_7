import os
import unittest

from app.io.output import print_to_console, write_to_file_builtin


class TestOutputFunctions(unittest.TestCase):
    def setUp(self):
        """Set up preconditions before each test."""
        if not os.path.exists("data"):
            os.makedirs("data")
        self.test_file = "data/output.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_print_to_console_exists(self):
        """Test that print_to_console is a callable function."""
        self.assertTrue(callable(print_to_console))

    def test_print_to_console_accepts_string(self):
        """Test that print_to_console handles a string input without raising an error."""
        try:
            print_to_console("Test string")
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"print_to_console raised an exception: {e}")

    def test_print_to_console_none_input(self):
        """Test that print_to_console handles None input."""
        try:
            print_to_console(None)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"print_to_console raised an exception with None: {e}")

    def test_write_to_file_builtin_exists(self):
        """Test that write_to_file_builtin is a callable function."""
        self.assertTrue(callable(write_to_file_builtin))

    def test_write_to_file_builtin_writes_string_default(self):
        """Test that write_to_file_builtin writes a string to the default file."""
        test_text = "Hello, world!"
        write_to_file_builtin(test_text)
        with open(self.test_file, "r") as file:
            content = file.read()
        self.assertEqual(content, test_text)

    def test_write_to_file_builtin_overwrites(self):
        """Test that write_to_file_builtin overwrites the file with new content."""
        write_to_file_builtin("Initial content")
        new_text = "Overwritten content"
        write_to_file_builtin(new_text)
        with open(self.test_file, "r") as file:
            content = file.read()
        self.assertEqual(content, new_text)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
