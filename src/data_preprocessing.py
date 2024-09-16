import os
from typing import List
import re

class DataPreprocessor:
    """
    A class to preprocess legal documents by cleaning and structuring the text.

    Methods:
    --------
    load_text(file_path: str) -> str:
        Loads the content of a text file.
    
    clean_text(text: str) -> str:
        Cleans the input text by removing unwanted characters and redundant spaces.
    
    preprocess_documents(raw_dir: str, processed_dir: str):
        Preprocesses all text files in the raw directory and saves them in the processed directory.
    """
    
    def __init__(self):
        pass

    def load_text(self, file_path: str) -> str:
        """Loads text from a given file path."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def clean_text(self, text: str) -> str:
        """Cleans the text by removing unwanted characters and extra whitespace."""
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        return text.strip()

    def preprocess_documents(self, raw_dir: str, processed_dir: str):
        """Preprocess all documents from the raw directory and save them to the processed directory."""
        if not os.path.exists(processed_dir):
            os.makedirs(processed_dir)

        for file_name in os.listdir(raw_dir):
            raw_file_path = os.path.join(raw_dir, file_name)
            processed_file_path = os.path.join(processed_dir, file_name)

            text = self.load_text(raw_file_path)
            cleaned_text = self.clean_text(text)

            with open(processed_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

if __name__ == "__main__":
    preprocessor = DataPreprocessor()
    raw_data_path = "../data/raw/"
    processed_data_path = "../data/processed/"
    preprocessor.preprocess_documents(raw_data_path, processed_data_path)
