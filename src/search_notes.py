import os  # Import the os module to handle file and directory operations
import re  # Import the re module to perform regular expression operations

from . import NOTES_DIR  # Directory where all the notes are stored

def search_notes(keyword):
    """
    Searches for notes that contain a specific keyword in their content.

    This function iterates through all note files in the `NOTES_DIR` directory, reads the content
    of each file, and checks if the specified keyword is present. It performs a case-insensitive 
    search and collects filenames of notes that contain the keyword.

    Parameters:
        keyword (str): The keyword to search for in the note files.

    Returns:
        list of str: A list of filenames (strings) of notes that contain the keyword.
    """
    notes = []  # Initialize an empty list to store filenames of notes containing the keyword
    
    # Iterate over each file in the notes directory
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith(".txt"):  # Check if the file is a text file
            # Construct the full file path and open the file in read mode
            with open(os.path.join(NOTES_DIR, filename), 'r') as f:
                content = f.read()  # Read the entire content of the file
                
                # Search for the keyword in the file content, ignoring case
                if re.search(keyword, content, re.IGNORECASE):
                    notes.append(filename)  # Add the filename to the list if the keyword is found
    
    return notes  # Return the list of filenames containing the keyword
