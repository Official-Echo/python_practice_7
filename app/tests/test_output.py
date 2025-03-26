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

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
