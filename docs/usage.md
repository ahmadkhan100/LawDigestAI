# Usage Guide

## Preprocessing Legal Documents

To preprocess legal documents, use the `DataPreprocessor` class:

```python
from src.data_preprocessing import DataPreprocessor

preprocessor = DataPreprocessor()
preprocessor.preprocess_documents('data/raw', 'data/processed')
```

This will clean and preprocess all documents from the `data/raw` directory and save them as JSON files in the `data/processed` directory.

## Summarizing Legal Documents

To summarize preprocessed legal documents, use the `LegalSummarizer` class:

```python
from src.summarization import LegalSummarizer

summarizer = LegalSummarizer()
summarizer.summarize_directory('data/processed', 'data/summaries')
```

This will generate summaries of all documents in the `data/processed` directory and save them in `data/summaries`.

---

For further details on model training, preprocessing, and summarization, refer to the source code documentation.
