import os  # Import the os module to handle file and directory operations

from . import NOTES_DIR  # Directory where all the notes are stored

def list_all_notes():
    """
    Lists all note files in the specified notes directory.

    This function retrieves all filenames in the `NOTES_DIR` directory that end with the ".txt" 
    extension, which indicates that they are note files.

    Returns:
        list of str: A list of filenames (strings) of all note files in the notes directory.
    """
    # List all files in the notes directory that have a ".txt" extension
    return [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
