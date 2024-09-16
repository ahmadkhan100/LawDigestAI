import os
import re
import json
from typing import List, Dict

class DataPreprocessor:
    """
    A class to preprocess legal documents by performing cleaning, tokenization, and structure extraction.

    Methods:
    --------
    load_text(file_path: str) -> str:
        Loads the content of a text file.
    
    clean_text(text: str) -> str:
        Cleans the input text by removing unwanted characters, extra spaces, and converting to lowercase.
    
    tokenize_text(text: str) -> List[str]:
        Splits text into a list of tokens (words).
    
    extract_sections(text: str) -> Dict[str, str]:
        Extracts legal document sections such as clauses, agreements, and obligations.
    
    preprocess_documents(raw_dir: str, processed_dir: str):
        Preprocesses all text files in the raw directory and saves them as structured JSON in the processed directory.
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
        text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        return text.strip()

    def tokenize_text(self, text: str) -> List[str]:
        """Tokenizes the text by splitting it into words."""
        return text.split()

    def extract_sections(self, text: str) -> Dict[str, str]:
        """
        Extracts important sections of a legal document based on simple regex patterns. 
        This can be customized further for legal structure.
        """
        sections = {}
        # Example of section extraction - can be customized for legal documents
        sections['clauses'] = re.findall(r'clause \d+:\s(.*?)\.', text)
        sections['agreements'] = re.findall(r'agreement\s(.*?)\.', text)
        sections['obligations'] = re.findall(r'obligation\s(.*?)\.', text)
        return sections

    def preprocess_documents(self, raw_dir: str, processed_dir: str):
        """Preprocess all documents from the raw directory and save them as structured JSON in the processed directory."""
        if not os.path.exists(processed_dir):
            os.makedirs(processed_dir)

        for file_name in os.listdir(raw_dir):
            raw_file_path = os.path.join(raw_dir, file_name)
            processed_file_path = os.path.join(processed_dir, f"{file_name}.json")

            # Load, clean, tokenize and extract sections from the document
            text = self.load_text(raw_file_path)
            cleaned_text = self.clean_text(text)
            tokens = self.tokenize_text(cleaned_text)
            sections = self.extract_sections(cleaned_text)

            # Save processed data as JSON
            processed_data = {
                'file_name': file_name,
                'cleaned_text': cleaned_text,
                'tokens': tokens,
                'sections': sections
            }
            with open(processed_file_path, 'w', encoding='utf-8') as file:
                json.dump(processed_data, file, indent=4)

if __name__ == "__main__":
    preprocessor = DataPreprocessor()
    raw_data_path = "../data/raw/"
    processed_data_path = "../data/processed/"
    preprocessor.preprocess_documents(raw_data_path, processed_data_path)
