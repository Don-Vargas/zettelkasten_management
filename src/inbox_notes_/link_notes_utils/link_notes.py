"""
This module provides utilities for managing notes within a Zettelkasten system.

It includes functions for finding and linking notes based on their unique identifiers (ZK_UID),
as well as for parsing and converting note data into a structured `NoteModel` format.

Classes:
    - NoteModel: Represents a note in the Zettelkasten system.
    - NoteIdentifiers: Holds the unique identifiers for a note.
    - NoteLinks: Manages forward and backward links between notes.
    - NoteMetadata: Contains metadata for a note, such as references and tags.
    - NoteContent: Holds the content and title of a note.

Functions:
    - find_note_filepath(note_uid, directories): Searches for a note file in specified directories
        based on its ZK_UID.
    - link_forward_notes(note_uid1, linked_uids, directories): Adds forward links to a note and
        updates backward links in the linked notes.
    - link_backward_notes(note_uid, linked_uids, address): Adds backward links to a note based on 
        its ZK_UID.
    - parse_note_data(note_data): Parses raw note data into a dictionary using predefined 
        section keywords.
    - dict_to_note_model(parsed_dict): Converts a dictionary of parsed note data into a 
        `NoteModel` instance.

Usage:
    This module is intended for use within a Zettelkasten system where notes are linked together 
    based on their unique identifiers. It facilitates the management of note files, including 
    finding, linking, and parsing notes.

Dependencies:
    - `os`: For file and directory operations.
    - `re`: For regular expression operations, used in parsing note data.
    - `datetime`: For handling date and time information.

Author:
    [Your Name]

License:
    [Your License]
"""
import os

from src.inbox_notes_.link_notes_utils.link_creation_utils import (
    find_note_filepath, 
    parse_note_data
    )

def link_note_forward(note_uid1, linked_uids, directories):
    """
    Adds forward links to a note and updates backward links in the linked notes within
    the Zettelkasten system.

    This function locates a note by its unique identifier (ZK_UID) in the specified 
    directories, appends a list of UIDs (representing links to other notes) to the 
    forward links section of the note, and also updates the backward links in each 
    linked note.

    Parameters:
        note_uid1 (str): The ZK_UID of the note to which forward links will be added.
        linked_uids (list of dict): A list of dictionaries representing notes to be linked.
                                    Each dictionary must contain:
                                    - 'ZK_UID' (str): The unique identifier of the linked note.
                                    - 'Description' (str): A description of the link.
        directories (list of str, optional): A list of directories to search for the notes.
                                             Defaults to [NOTES_DIR_INBOX, NOTES_DIR_PERMA] 
                                             if not provided.

    Returns:
        None

    Notes:
        - If the note identified by `note_uid1` or any linked notes are not found, an error message
          will be printed.
        - The function updates both the forward links in the main note and the backward links 
          in each linked note, and then saves the changes to the corresponding files.
    """
    # Find the file path for note_uid1
    filepath1 = find_note_filepath(note_uid1, directories)

    if not filepath1:
        print(f"Note with ZK_UID {note_uid1} not found.")
        return

    # Load the existing note from the file
    with open(filepath1, 'r', encoding='utf-8') as f:
        note_data1 = f.read()

    # Parse the note into a NoteModel instance
    note1 = parse_note_data(note_data1)

    # Add the forward linked UIDs to the note
    for link in linked_uids:
        note1.add_forward_link(link['ZK_UID'], link['Description'])

        # Find the file path for the linked note (note_uid0)
        filepath0 = find_note_filepath(link['ZK_UID'], directories)

        if filepath0:
            # Load the linked note
            with open(filepath0, 'r', encoding='utf-8') as f:
                note_data0 = f.read()

            # Parse the linked note into a NoteModel instance
            note0 = parse_note_data(note_data0)

            # Add the backward link in the linked note
            note0.add_backward_link(note_uid1, f"Linked from: {note1.contents.title}")

            # Save the updated linked note back to the file
            with open(filepath0, 'w', encoding='utf-8') as f:
                f.write(str(note0))
        else:
            print(f"Linked note with ZK_UID {link['ZK_UID']} not found.")

    # Save the updated note1 back to the file
    with open(filepath1, 'w', encoding='utf-8') as f:
        f.write(str(note1))

def link_backward_notes(note_uid, linked_uids, address):
    """
    Adds backward links to a note within the Zettelkasten system.

    This function searches for a note by its unique identifier (ZK_UID) in the notes directory,
    then appends a list of UIDs (representing links from other notes) to the backward links section
    in the note file. This allows the user to establish backward connections from related notes.

    Parameters:
        note_uid (str): The ZK_UID of the note that will have backward links added to it.
        linked_uids (list of dict): A list of dictionaries representing the notes that should be 
                                    linked, with each dictionary containing a 
                                    'ZK_UID' and a 'Description'.

    Returns:
        None
    """
    # Find the filename of the note that starts with the specified ZK_UID
    filename = [f for f in os.listdir(address) if f.startswith(note_uid)][0]

    # Construct the full file path to the note
    filepath = os.path.join(address, filename)

    # Load the existing note from the file
    with open(filepath, 'r', encoding='utf-8') as f:
        note_data = f.read()

    # Parse the note into a NoteModel instance
    note = parse_note_data(note_data)

    # Add the linked UIDs to the backward links list
    for link in linked_uids:
        note.add_backward_link(link['ZK_UID'], link['Description'])

    # Save the updated note back to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(note))
