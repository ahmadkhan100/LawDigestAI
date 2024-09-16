import unittest
import os
from src.model_training import SummarizationModel

class TestSummarizationModel(unittest.TestCase):
    def setUp(self):
        """Set up the test environment and initialize SummarizationModel."""
        self.model_trainer = SummarizationModel()
        self.model_save_dir = "./test_data/model/"
        os.makedirs(self.model_save_dir, exist_ok=True)
    
    def tearDown(self):
        """Clean up after tests by removing the model directory."""
        if os.path.exists(self.model_save_dir):
            for file in os.listdir(self.model_save_dir):
                os.remove(os.path.join(self.model_save_dir, file))
            os.rmdir(self.model_save_dir)

    def test_fine_tune_model(self):
        """Test the fine-tune model method."""
        train_documents = ["Party A agrees to fulfill obligations."]
        train_summaries = ["Party A agrees to obligations."]
        self.model_trainer.fine_tune_model(train_documents, train_summaries)
        # Since the method prints training loss, we can't assert much here, 
        # but you can ensure no errors during training.

    def test_save_model(self):
        """Test saving the fine-tuned model."""
        self.model_trainer.save_model(self.model_save_dir)
        self.assertTrue(os.path.exists(self.model_save_dir))
        self.assertTrue(os.path.exists(os.path.join(self.model_save_dir, "config.json")))

    def test_load_model(self):
        """Test loading the fine-tuned model."""
        self.model_trainer.save_model(self.model_save_dir)
        self.model_trainer.load_model(self.model_save_dir)
        self.assertTrue(self.model_trainer.model is not None)

if __name__ == "__main__":
    unittest.main()
