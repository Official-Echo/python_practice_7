import os
import unittest
from unittest.mock import patch

from app.io.input import read_from_console


class TestInputFunctions(unittest.TestCase):
    def setUp(self):
        """Set up preconditions before each test."""
        if not os.path.exists("data"):
            os.makedirs("data")
        self.sample_txt = "data/sample.txt"
        with open(self.sample_txt, "w") as file:
            file.write("Sample text content")
        self.sample_csv = "data/sample.csv"
        with open(self.sample_csv, "w") as file:
            file.write("col1,col2\n1,2\n3,4")

    def test_read_from_console_exists(self):
        """Test that read_from_console is a callable function."""
        self.assertTrue(callable(read_from_console))

    def test_read_from_console_returns_string(self):
        """Test that read_from_console returns a string with test input."""
        with patch("builtins.input", return_value="User input"):
            result = read_from_console()
            self.assertEqual(result, "User input")

    def test_read_from_console_prompt(self):
        """Test that read_from_console prompts with 'Enter text: '."""
        with patch("builtins.input", return_value="Test") as test_input:
            read_from_console()
            test_input.assert_called_once_with("Enter text: ")

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.sample_txt):
            os.remove(self.sample_txt)
        if os.path.exists(self.sample_csv):
            os.remove(self.sample_csv)


if __name__ == "__main__":
    unittest.main()
