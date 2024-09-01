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
