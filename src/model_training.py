from transformers import BartTokenizer, BartForConditionalGeneration
import torch
import os
from typing import List

class SummarizationModel:
    """
    A class to fine-tune a pre-trained transformer model for legal document summarization.
    
    Methods:
    --------
    fine_tune_model(train_data: List[str], train_summaries: List[str]):
        Fine-tunes the pre-trained model using the provided training data.
    
    save_model(save_dir: str):
        Saves the fine-tuned model to the specified directory.
    
    load_model(load_dir: str):
        Loads a previously saved model from the specified directory.
    """
    
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=1e-5)

    def fine_tune_model(self, train_data: List[str], train_summaries: List[str]):
        """Fine-tune the model using a custom dataset of legal documents and summaries."""
        inputs = self.tokenizer(train_data, return_tensors='pt', max_length=1024, truncation=True, padding=True)
        labels = self.tokenizer(train_summaries, return_tensors='pt', max_length=1024, truncation=True, padding=True)
        
        self.model.train()
        outputs = self.model(input_ids=inputs.input_ids, labels=labels.input_ids)
        loss = outputs.loss
        loss.backward()
        self.optimizer.step()
        
        print(f"Training loss: {loss.item()}")

    def save_model(self, save_dir: str):
        """Saves the fine-tuned model to the specified directory."""
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        self.model.save_pretrained(save_dir)
        self.tokenizer.save_pretrained(save_dir)
        print(f"Model saved to {save_dir}")

    def load_model(self, load_dir: str):
        """Loads a previously saved model from the specified directory."""
        self.model = BartForConditionalGeneration.from_pretrained(load_dir)
        self.tokenizer = BartTokenizer.from_pretrained(load_dir)
        print(f"Model loaded from {load_dir}")

if __name__ == "__main__":
    # Example usage
    train_documents = ["Document text 1...", "Document text 2..."]
    train_summaries = ["Summary 1...", "Summary 2..."]
    
    model_trainer = SummarizationModel()
    model_trainer.fine_tune_model(train_documents, train_summaries)
    
    model_save_dir = "../models/fine_tuned_bart/"
    model_trainer.save_model(model_save_dir)
