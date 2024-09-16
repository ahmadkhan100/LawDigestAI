import os
import logging

def ensure_directory_exists(directory: str):
    """Ensure the directory exists, and if not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")
    else:
        logging.info(f"Directory already exists: {directory}")

def setup_logging(log_file: str):
    """Sets up logging for the application."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging is set up.")
