import os  # Import the os module to handle file and directory operations

from . import NOTES_DIR  # Directory where all the notes are stored

def link_notes(note_uid, linked_uids):
    """
    Adds links to other notes within a given note by appending their UIDs to the note file.

    This function searches for a note by its unique identifier (UID) in the notes directory,
    then appends a list of UIDs (representing links to other notes) to the file. This allows
    the user to establish connections between related notes in a Zettelkasten system.

    Parameters:
        note_uid (str): The UID of the note that will have links added to it.
        linked_uids (list of str): A list of UIDs representing the notes that should be linked 
                                   to the note identified by note_uid.

    Returns:
        None
    """
    # Find the filename of the note that starts with the specified UID
    filename = [f for f in os.listdir(NOTES_DIR) if f.startswith(note_uid)][0]
    
    # Construct the full file path to the note
    filepath = os.path.join(NOTES_DIR, filename)
    
    # Open the note file in append mode
    with open(filepath, 'a') as f:
        # Write a header indicating the start of the linked notes section
        f.write(f"\nLinks to Other Notes:\n")
        
        # Iterate over the list of linked UIDs and write each one to the file
        for uid in linked_uids:
            f.write(f"{uid}\n")
