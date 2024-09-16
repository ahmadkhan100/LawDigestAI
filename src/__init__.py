
"""
LawDigestAI package initializer.
This package includes modules for preprocessing legal documents, summarizing them, and training summarization models.
"""

from .data_preprocessing import DataPreprocessor
from .summarization import LegalSummarizer
from .utils import ensure_directory_exists

__all__ = ['DataPreprocessor', 'LegalSummarizer', 'ensure_directory_exists']
