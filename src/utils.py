import os

def ensure_directory_exists(directory: str):
    """Ensure the directory exists, and if not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)
