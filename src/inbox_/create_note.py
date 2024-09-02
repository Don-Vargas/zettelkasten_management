"""
create_note.py
------------

This package creates a new note.

Functions:
- generate_zk_uid: [Brief description of module1]
- create_note: [Brief description of module2]

Key Features:
- creates new notes.

Usage:
called in main.

Dependencies:
. import UID_FORMAT, NOTES_DIR_INBOX: Imports UID_FORMAT and NOTES_DIR_INBOX from __init__.py
.note_model import NoteModel: Imports the NoteModel class
os
datetime
uuid: Imports the uuid module to generate UUIDs

Author:
Hector Alejandro Vargas Gutierrez

License:
[Specify the license under which the package is distributed, if applicable.]

"""
import os
import datetime
import uuid

from .. import UID_FORMAT, NOTES_DIR_INBOX
from ..utils.note_model import NoteModel

# Generate ZK_UID
def generate_zk_uid():
    """
    Generates a unique Zettelkasten identifier (ZK_UID) based on the current timestamp.

    The ZK_UID is created using the current date and time formatted according to the
    UID_FORMAT string imported from the __init__.py file. This ensures that each ZK_UID is unique.

    Returns:
        str: A string representing the unique Zettelkasten identifier.
    """
    return datetime.datetime.now().strftime(UID_FORMAT)

# Create a New Note
def create_note(note: NoteModel):
    """
    Creates a new note with a unique filename and saves it to the specified notes directory.

    The note is saved as a .txt file with a filename that includes a UUID and 
    the note's title (spaces replaced with underscores). The content of the 
    note includes the title, ZK_UID, main content, and optionally references, tags, 
    links to other notes (forward and backward), and additional thoughts.

    Parameters:
        title (str): The title of the note.
        content (str): The main content of the note.
        tags (list of str, optional): A list of tags associated with the note.
        references (str, optional): References or citations related to the note.
        links_forward (list of dict, optional): Forward links to other notes by their ZK_UIDs and 
                                                descriptions.
        links_backward (list of dict, optional): Backward links from other notes by their ZK_UIDs 
                                                and descriptions.
        thoughts (str, optional): Additional thoughts or connections related to the note.

    Returns:
        None
    """
    # Generate a UUID and ZK_UID for the note
    note_uuid = str(uuid.uuid4())
    zk_uid = generate_zk_uid()

    note.identifiers.uuid = note_uuid

    # Create a filename based on the ZK_UID and title, replacing spaces with underscores
    filename = f"{zk_uid}-{note.contents.title.replace(' ', '_')}.txt"

    # Construct the full file path in the "notes" directory
    filepath = os.path.join(NOTES_DIR_INBOX, filename)

    # Open the file in write mode and write the note's content using the NoteModel's __str__ method
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(note))

    print(f"Note created successfully with UUID: {note_uuid}")
