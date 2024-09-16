import unittest
import os
from src.utils import ensure_directory_exists, setup_logging

class TestUtils(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.test_dir = "./test_data/test_dir/"
        self.log_file = "./test_data/test_log.log"
        os.makedirs("./test_data/", exist_ok=True)
    
    def tearDown(self):
        """Clean up after tests by removing test directories and log files."""
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
    
    def test_ensure_directory_exists(self):
        """Test that ensure_directory_exists creates a directory if it doesn't exist."""
        ensure_directory_exists(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))
    
    def test_setup_logging(self):
        """Test that setup_logging creates a log file and writes logs."""
        setup_logging(self.log_file)
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, 'r') as log:
            log_content = log.read()
        self.assertIn("Logging is set up.", log_content)

if __name__ == "__main__":
    unittest.main()
