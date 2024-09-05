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
import re

from datetime import datetime

from ..utils.note_model import NoteModel, NoteIdentifiers, NoteLinks, NoteMetadata, NoteContent

def find_note_filepath(note_uid, directories):
    """
    Search for the note file in the given directories based on the ZK_UID.

    Args:
        note_uid (str): The ZK_UID of the note.
        directories (list of str): A list of directories to search.

    Returns:
        str: The full file path of the note if found, otherwise None.
    """
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.startswith(note_uid):
                return os.path.join(directory, filename)
    return None

def link_forward_notes(note_uid1, linked_uids, directories):
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

def parse_note_data(note_data):
    """
    Parse the raw note data into a dictionary using predefined section keywords as delimiters.

    Args:
        note_data (str): The raw content of the note file.

    Returns:
        dict: A dictionary where keys are section names and values are the corresponding content.
    """
    # Define the section keywords that delimit each part of the note
    sections = [
        "uuid",
        "Title",
        "ZK_UID",
        "Date",
        "Content",
        "References",
        "Tags",
        "Links forward to Other Notes",
        "Linked backward from Other Notes",
        "Thoughts/Connections"
    ]

    # Create a regex pattern to match each section
    pattern = re.compile(rf"({'|'.join(sections)}):?")

    # Split the note data into sections based on the defined pattern
    splits = pattern.split(note_data)

    # Initialize a dictionary to hold the parsed note data
    note_dict = {}

    # Iterate over the splits to populate the dictionary
    for i in range(1, len(splits), 2):
        section_name = splits[i].strip()
        content = splits[i + 1].strip()
        note_dict[section_name] = content

    # Separate forward and backward links into their own lists
    if "Links forward to Other Notes" in note_dict:
        pattern = r"ZK_UID \d{3,4}[A-Z]-[0-9.]+-[0-9]{3} \([^)]+\)"
        links = re.findall(pattern, note_dict["Links forward to Other Notes"])
        note_dict["Links forward to Other Notes"] = links

    if "Linked backward from Other Notes" in note_dict:
        pattern = r"ZK_UID \d{3,4}[A-Z]-[0-9.]+-[0-9]{3} \([^)]+\)"
        linked_backward_notes = re.findall(pattern, note_dict["Linked backward from Other Notes"])
        note_dict["Linked backward from Other Notes"] = linked_backward_notes

    return dict_to_note_model(note_dict)


def dict_to_note_model(parsed_dict):
    """
    Convert a dictionary of parsed note data into a NoteModel instance.

    Args:
        parsed_dict (dict): A dictionary containing the parsed note data.

    Returns:
        NoteModel: An instance of NoteModel populated with the data from the dictionary.
    """
    def parse_links(link_data):
        """Helper function to parse links."""
        links = []
        for link in link_data.split("\n"):
            if link.startswith("Related to: ZK_UID"):
                uid_desc = link.split("ZK_UID ")[1].split(" (")
                links.append({"ZK_UID": uid_desc[0], "Description": uid_desc[1][:-1]})
        return links

    def parse_list(data, delimiter=" "):
        """Helper function to parse a list from a string."""
        return data.split(delimiter) if data else []

    # Extract data from the dictionary
    title = parsed_dict.get("Title", "")
    zk_uid = parsed_dict.get("ZK_UID", "")
    content = parsed_dict.get("Content", "")
    date = parsed_dict.get("Date", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    references = parse_list(parsed_dict.get("References", ""), ", ")
    tags = parse_list(parsed_dict.get("Tags", " "))

    forward_links = parse_links(parsed_dict.get("Links forward to Other Notes", ""))
    backward_links = parse_links(parsed_dict.get("Linked backward from Other Notes", ""))

    thoughts_connections = parsed_dict.get("Thoughts/Connections", "")

    # Create and return the NoteModel instance
    return NoteModel(
        identifiers=NoteIdentifiers(
            uuid=parsed_dict.get("UUID", ""),
            zk_uid=zk_uid
        ),
        date=date,
        metadata=NoteMetadata(
            references=references,
            tags=tags
        ),
        links=NoteLinks(
            forward=forward_links,
            backward=backward_links
        ),
        contents=NoteContent(
            title=title,
            content=content,
            thoughts_connections=thoughts_connections
        )
    )
