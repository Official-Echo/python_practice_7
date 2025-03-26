import os
import unittest
from unittest.mock import patch

import pandas as pd

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

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.sample_txt):
            os.remove(self.sample_txt)
        if os.path.exists(self.sample_csv):
            os.remove(self.sample_csv)


if __name__ == "__main__":
    unittest.main()
