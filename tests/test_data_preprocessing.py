import unittest
import os
import json
from src.data_preprocessing import DataPreprocessor

class TestDataPreprocessor(unittest.TestCase):
    def setUp(self):
        """Set up the test environment and initialize the DataPreprocessor."""
        self.preprocessor = DataPreprocessor()
        self.test_raw_dir = "./test_data/raw/"
        self.test_processed_dir = "./test_data/processed/"
        os.makedirs(self.test_raw_dir, exist_ok=True)
        os.makedirs(self.test_processed_dir, exist_ok=True)

        # Create a sample raw legal document
        self.sample_text = "CLAUSE 1: Party A agrees to do X. OBLIGATION 1: Party B agrees to do Y."
        with open(os.path.join(self.test_raw_dir, "test_doc.txt"), "w") as file:
            file.write(self.sample_text)
    
    def tearDown(self):
        """Clean up after tests by removing test directories."""
        for root_dir in [self.test_raw_dir, self.test_processed_dir]:
            for file in os.listdir(root_dir):
                os.remove(os.path.join(root_dir, file))
            os.rmdir(root_dir)

    def test_load_text(self):
        """Test that the load_text method correctly loads text from a file."""
        loaded_text = self.preprocessor.load_text(os.path.join(self.test_raw_dir, "test_doc.txt"))
        self.assertEqual(loaded_text, self.sample_text)
    
    def test_clean_text(self):
        """Test the clean_text method."""
        dirty_text = "This   is   a    TEST!!  "
        cleaned_text = self.preprocessor.clean_text(dirty_text)
        self.assertEqual(cleaned_text, "this is a test")
    
    def test_tokenize_text(self):
        """Test the tokenize_text method."""
        tokens = self.preprocessor.tokenize_text("This is a test.")
        self.assertEqual(tokens, ["this", "is", "a", "test"])

    def test_extract_sections(self):
        """Test the extract_sections method to ensure correct section extraction."""
        sections = self.preprocessor.extract_sections(self.sample_text.lower())
        self.assertIn("clauses", sections)
        self.assertIn("obligations", sections)
        self.assertEqual(len(sections["clauses"]), 1)
        self.assertEqual(len(sections["obligations"]), 1)

    def test_preprocess_documents(self):
        """Test the preprocess_documents method."""
        self.preprocessor.preprocess_documents(self.test_raw_dir, self.test_processed_dir)
        processed_file_path = os.path.join(self.test_processed_dir, "test_doc.txt.json")
        
        self.assertTrue(os.path.exists(processed_file_path))
        
        # Check if processed file contains cleaned text, tokens, and sections
        with open(processed_file_path, "r") as file:
            processed_data = json.load(file)
        self.assertIn("cleaned_text", processed_data)
        self.assertIn("tokens", processed_data)
        self.assertIn("sections", processed_data)
        self.assertEqual(len(processed_data["tokens"]), 9)  # Ensure tokenization works

if __name__ == "__main__":
    unittest.main()
