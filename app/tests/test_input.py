import os
import unittest
import pandas as pd
from unittest.mock import patch

from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas


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

    def test_read_from_file_builtin_exists(self):
        """Test that read_from_file_builtin is a callable function."""
        self.assertTrue(callable(read_from_file_builtin))

    def test_read_from_file_builtin_reads_default(self):
        """Test that read_from_file_builtin reads from the default file."""
        result = read_from_file_builtin()
        self.assertEqual(result, "Sample text content")

    def test_read_from_file_builtin_returns_string(self):
        """Test that read_from_file_builtin returns a string."""
        result = read_from_file_builtin(self.sample_txt)
        self.assertIsInstance(result, str)

    def test_read_from_file_pandas_exists(self):
        """Test that read_from_file_pandas is a callable function."""
        self.assertTrue(callable(read_from_file_pandas))

    def test_read_from_file_pandas_reads_default(self):
        """Test that read_from_file_pandas reads from the default CSV file."""
        result = read_from_file_pandas()
        expected = pd.read_csv(self.sample_csv).to_string()
        self.assertEqual(result, expected)

    def test_read_from_file_pandas_returns_string(self):
        """Test that read_from_file_pandas returns a string."""
        result = read_from_file_pandas(self.sample_csv)
        self.assertIsInstance(result, str)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.sample_txt):
            os.remove(self.sample_txt)
        if os.path.exists(self.sample_csv):
            os.remove(self.sample_csv)


if __name__ == "__main__":
    unittest.main()
