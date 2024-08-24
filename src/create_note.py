from . import UID_FORMAT, NOTES_DIR  # Import UID_FORMAT and NOTES_DIR from __init__.py
import os
import datetime

# Generate UID
def generate_uid():
    """
    Generates a unique identifier (UID) based on the current timestamp.

    The UID is created using the current date and time formatted according 
    to the UID_FORMAT string imported from the __init__.py file. This ensures 
    that each UID is unique.

    Returns:
        str: A string representing the unique identifier.
    """
    return datetime.datetime.now().strftime(UID_FORMAT)

# Create a New Note
def create_note(title, content, tags=None, references=None, links=None, thoughts=None):
    """
    Creates a new note with a unique filename and saves it to the specified notes directory.

    The note is saved as a .txt file with a filename that includes a UID and 
    the note's title (spaces replaced with underscores). The content of the 
    note includes the title, UID, main content, and optionally references, tags, 
    links to other notes, and additional thoughts.

    Parameters:
        title (str): The title of the note.
        content (str): The main content of the note.
        tags (list of str, optional): A list of tags associated with the note.
        references (str, optional): References or citations related to the note.
        links (str, optional): Links to other notes by their UIDs.
        thoughts (str, optional): Additional thoughts or connections related to the note.

    Returns:
        None
    """
    # Generate a unique identifier for the note
    uid = generate_uid()
    
    # Create a filename based on the UID and title, replacing spaces with underscores
    filename = f"{uid}-{title.replace(' ', '_')}.txt"
    
    # Construct the full file path in the "notes" directory
    filepath = os.path.join(NOTES_DIR, filename)
    
    # Open the file in write mode and start writing the note's content
    with open(filepath, 'w') as f:
        f.write(f"Title: {title}\n")  # Write the note's title
        f.write(f"UID: {uid}\n\n")  # Write the unique identifier
        f.write(f"Content:\n{content}\n\n")  # Write the main content of the note
        
        # Optionally include references if provided
        if references:
            f.write(f"References:\n{references}\n\n")
        
        # Optionally include tags if provided
        if tags:
            f.write(f"Tags: {' '.join(tags)}\n\n")
        
        # Optionally include links to other notes if provided
        if links:
            f.write(f"Links to Other Notes:\n{links}\n\n")
        
        # Optionally include additional thoughts if provided
        if thoughts:
            f.write(f"Thoughts/Connections:\n{thoughts}\n")
