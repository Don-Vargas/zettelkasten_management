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
from src import NOTES_DIR_INBOX
from src.utils.note_utils.note_model import NoteModel
from src.inbox_notes_.new_note_utils import generate_zk_uid, generate_uuid

def new_note(note: NoteModel, directory: str = NOTES_DIR_INBOX):
    """
    Creates a new note with a unique filename and saves it to the specified directory.

    Parameters:
        note (NoteModel): The note object containing all note information.
        directory (str): The directory where the note should be saved. Defaults to NOTES_DIR_INBOX.

    Returns:
        None
    """
    # Assign UUID and ZK_UID to the note
    note.identifiers.uuid = generate_uuid()
    note.identifiers.zk_uid = generate_zk_uid()

    # Create a filename based on the ZK_UID and title
    filename = f"{note.identifiers.zk_uid}-{note.contents.title.replace(' ', '_')}.txt"
    filepath = os.path.join(directory, filename)

    # Save the note to the specified directory
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(note))

    print(f"Note created successfully with UUID: {note.identifiers.uuid}")
