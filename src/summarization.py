from transformers import pipeline
import os
import json

class LegalSummarizer:
    """
    A class for summarizing legal documents using a pre-trained transformer model.

    Methods:
    --------
    summarize(text: str, max_length: int = 150) -> str:
        Summarizes the input text using the pre-trained model.
    
    summarize_file(file_path: str) -> str:
        Loads text from a file and generates its summary.
    
    summarize_json_file(file_path: str) -> str:
        Summarizes the cleaned text from a JSON file created by the preprocessor.
    
    summarize_directory(raw_dir: str, summary_dir: str):
        Summarizes all text files in a directory and saves them in the summary directory.
    """
    
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    def summarize(self, text: str, max_length: int = 150) -> str:
        """Generates a summary for the given text using the pre-trained model."""
        return self.summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

    def summarize_file(self, file_path: str) -> str:
        """Generates a summary for the text in the specified file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return self.summarize(text)

    def summarize_json_file(self, file_path: str) -> str:
        """Generates a summary for the cleaned text in a JSON file produced by the DataPreprocessor."""
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            cleaned_text = data['cleaned_text']
        return self.summarize(cleaned_text)

    def summarize_directory(self, raw_dir: str, summary_dir: str):
        """Summarizes all text files in a directory and saves them in the summary directory."""
        if not os.path.exists(summary_dir):
            os.makedirs(summary_dir)
        
        for file_name in os.listdir(raw_dir):
            raw_file_path = os.path.join(raw_dir, file_name)
            summary_file_path = os.path.join(summary_dir, f"summary_{file_name}")

            summary = self.summarize_json_file(raw_file_path)
            with open(summary_file_path, 'w', encoding='utf-8') as file:
                file.write(summary)

if __name__ == "__main__":
    summarizer = LegalSummarizer()
    raw_data_path = "../data/processed/"
    summary_data_path = "../data/summaries/"
    summarizer.summarize_directory(raw_data_path, summary_data_path)
