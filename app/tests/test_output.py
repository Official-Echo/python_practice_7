import os
import unittest

from app.io.output import print_to_console


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

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
