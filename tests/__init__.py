"""
Tests package initializer for the LawDigestAI project.
"""

# Import all test modules so they can be easily run by the test runner
from .test_data_preprocessing import TestDataPreprocessor
from .test_summarization import TestLegalSummarizer
from .test_utils import TestUtils
from .test_model_training import TestSummarizationModel

__all__ = [
    'TestDataPreprocessor', 
    'TestLegalSummarizer', 
    'TestUtils', 
    'TestSummarizationModel'
]
