"""
search_notes.py
------------

This package searches for all notes on inbox or permanent_notes directories.

Functions:
- search_notes: [Brief description of module1]

Key Features:
- searches for all notes on the system.

Usage:
called in main.

Dependencies:
os: Imports the os module to handle file and directory operations
re: Imports the re module to perform regular expression operations

Author:
Hector Alejandro Vargas Gutierrez

License:
[Specify the license under which the package is distributed, if applicable.]

"""
import os
import re

from typing import List, Tuple

def search_notes(keyword, address):
    """
    Searches for notes that contain a specific keyword in their content.

    This function iterates through all note files in the 
    address(`NOTES_DIR_INBOX`,`NOTES_DIR_PERMA`) directory, reads the content
    of each file, and checks if the specified keyword is present. It performs a case-insensitive 
    search and collects filenames of notes that contain the keyword.

    Parameters:
        keyword (str): The keyword to search for in the note files.

    Returns:
        list of str: A list of filenames (strings) of notes that contain the keyword.
    """
    notes = []# Initialize an empty list to store filenames of notes containing the keyword

    # Iterate over each file in the notes directory
    for filename in os.listdir(address):
        if filename.endswith(".txt"):  # Check if the file is a text file
            # Construct the full file path and open the file in read mode
            with open(os.path.join(address, filename), 'r', encoding='utf-8') as f:
                content = f.read()# Read the entire content of the file

                # Search for the keyword in the file content, ignoring case
                if re.search(keyword, content, re.IGNORECASE):
                    notes.append(filename)# Add the filename to the list if the keyword is found

    return notes  # Return the list of filenames containing the keyword

def list_all_titles(address: str) -> List[Tuple[str, str]]:
    """
    Lists all titles and their corresponding UUIDs of notes in the specified directory.

    This function iterates through all note files in the specified directory,
    extracts the title and UUID of each note, and returns a list of tuples containing
    the title and UUID.

    Parameters:
        address (str): The directory where note files are stored.

    Returns:
        List[Tuple[str, str]]: A list of tuples, where each tuple contains a title and
        its corresponding UUID.
    """
    titles_with_uuids = []  # Initialize an empty list to store tuples of (title, uuid)

    # Iterate over each file in the notes directory
    for filename in os.listdir(address):
        if filename.endswith(".txt"):  # Check if the file is a text file
            # Construct the full file path and open the file in read mode
            with open(os.path.join(address, filename), 'r', encoding='utf-8') as f:
                content = f.read()

                # Search for the title in the file content
                title_match = re.search(r'^Title: \s*(.*)$', content, re.MULTILINE)
                # Search for the UUID in the file content
                uuid_match = re.search(r'UUID: \s*(.*)$', content, re.MULTILINE)

                if title_match and uuid_match:
                    # Extract and clean the title and UUID
                    title = title_match.group(1).strip()
                    uuid = uuid_match.group(1).strip()
                    # Append the tuple (title, uuid) to the list
                    titles_with_uuids.append((title, uuid))

    return titles_with_uuids  # Return the list of tuples containing titles and UUIDs
    