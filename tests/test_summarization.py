import unittest
import os
import json
from src.summarization import LegalSummarizer

class TestLegalSummarizer(unittest.TestCase):
    def setUp(self):
        """Set up the test environment and initialize the LegalSummarizer."""
        self.summarizer = LegalSummarizer()
        self.test_processed_dir = "./test_data/processed/"
        self.test_summary_dir = "./test_data/summaries/"
        os.makedirs(self.test_processed_dir, exist_ok=True)
        os.makedirs(self.test_summary_dir, exist_ok=True)

        # Create a sample processed JSON file
        processed_data = {
            "cleaned_text": "party a agrees to perform obligations party b agrees to comply",
            "tokens": ["party", "a", "agrees", "to", "perform", "obligations", "party", "b", "agrees", "to", "comply"],
            "sections": {
                "clauses": ["party a agrees to perform obligations"],
                "obligations": ["party b agrees to comply"]
            }
        }
        with open(os.path.join(self.test_processed_dir, "test_doc.json"), "w") as file:
            json.dump(processed_data, file)

    def tearDown(self):
        """Clean up after tests by removing test directories."""
        for root_dir in [self.test_processed_dir, self.test_summary_dir]:
            for file in os.listdir(root_dir):
                os.remove(os.path.join(root_dir, file))
            os.rmdir(root_dir)

    def test_summarize(self):
        """Test the summarize method for generating summaries."""
        text = "Party A agrees to perform obligations, Party B agrees to comply."
        summary = self.summarizer.summarize(text)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)  # Ensure that the summary is not empty
    
    def test_summarize_file(self):
        """Test summarizing a text file."""
        file_path = os.path.join(self.test_processed_dir, "test_doc.json")
        summary = self.summarizer.summarize_json_file(file_path)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
    
    def test_summarize_directory(self):
        """Test summarizing all files in a directory."""
        self.summarizer.summarize_directory(self.test_processed_dir, self.test_summary_dir)
        summary_file_path = os.path.join(self.test_summary_dir, "summary_test_doc.json")
        self.assertTrue(os.path.exists(summary_file_path))
        with open(summary_file_path, 'r') as file:
            summary_text = file.read()
        self.assertIsInstance(summary_text, str)
        self.assertGreater(len(summary_text), 0)

if __name__ == "__main__":
    unittest.main()
