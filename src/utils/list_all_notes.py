"""
list_notes.py
-------------

This package provides functionality to list all note files within a specified directory and 
extract essential metadata such as UUID, title, and file name.

Functions:
- list_all_notes: Retrieves and returns a list of tuples containing the UUID, title, and file name 
                  of all note files in a given directory.

Key Features:
- Scans a directory for all text files associated with notes.
- Extracts metadata (UUID and title) from each note file.
- Returns structured information to assist with note management tasks.

Usage:
Typically used as part of a note management system, such as a Zettelkasten implementation.
Can be called directly in scripts to gather information about notes in a specified directory.

Dependencies:
- os: Imports the os module to handle file and directory operations.
- re: Imports the re module to perform regular expression operations.
- typing: Imports the typing module to specify type hints for function signatures.

Author:
Hector Alejandro Vargas Gutierrez

License:
[Specify the license under which the package is distributed, if applicable.]
"""

import os
import re
from typing import List, Tuple

def list_all_notes(address: str) -> List[Tuple[str, str, str]]:
    """
    Lists all note files in the specified notes directory and extracts the UUID, title, 
    and file name for each note.

    This function retrieves all filenames in the directory specified by the `address` parameter 
    that end with the ".txt" extension, reads the content to extract the UUID and title, and returns 
    a list of tuples containing the UUID, title, and file name.

    Args:
        address (str): The path to the directory where notes are stored. This is typically 
                       a directory path like `NOTES_DIR_INBOX` or `NOTES_DIR_PERMA`.

    Returns:
        List[Tuple[str, str, str]]: A list of tuples, where each tuple contains the UUID, title, 
        and file name of a note.
    """
    notes_info = []

    # Iterate over each file in the notes directory
    for filename in os.listdir(address):
        if filename.endswith(".txt"):  # Check if the file is a text file
            # Construct the full file path and open the file in read mode
            with open(os.path.join(address, filename), 'r', encoding='utf-8') as f:
                content = f.read()

                # Search for the UUID in the file content
                uuid_match = re.search(r'^UUID:\s*(.*)$', content, re.MULTILINE)
                # Search for the title in the file content
                title_match = re.search(r'^Title:\s*(.*)$', content, re.MULTILINE)

                if uuid_match and title_match:
                    uuid = uuid_match.group(1).strip()
                    title = title_match.group(1).strip()
                    notes_info.append((uuid, title, filename))  # Add the tuple to the list

    return notes_info  # Return the list of UUID, title, and file name
