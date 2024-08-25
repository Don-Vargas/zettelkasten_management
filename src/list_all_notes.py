"""
This module provides functionality to list all note files within a specified directory.

The primary purpose of this module is to assist in the management of notes stored in a 
Zettelkasten system. 
It contains a single function, `list_all_notes`, which scans a given directory for note files with 
the ".txt" extension and returns a list of these filenames.

Modules:
    os: Used to interact with the operating system, particularly for listing files in directories.

Functions:
    list_all_notes(address):
        Lists all note files in the specified directory.

        Args:
            address (str): The path to the directory where notes are stored. This is typically 
                           a directory path like `NOTES_DIR_INBOX` or `NOTES_DIR_PERMA`.

        Returns:
            list of str: A list of filenames (strings) of all note files in the specified directory.
"""
import os  # Import the os module to handle file and directory operations

def list_all_notes(address):
    """
    Lists all note files in the specified notes directory.

    This function retrieves all filenames in the directory specified by the `address` parameter 
    that end with the ".txt" extension, which indicates that they are note files.

    Args:
        address (str): The path to the directory where notes are stored. This is typically 
                       a directory path like `NOTES_DIR_INBOX` or `NOTES_DIR_PERMA`.

    Returns:
        list of str: A list of filenames (strings) of all note files in the specified directory.
    """
    # List all files in the notes directory that have a ".txt" extension
    return [f for f in os.listdir(address) if f.endswith(".txt")]
