import os
import re
from datetime import datetime

from src.utils.note_utils.note_model import (
    NoteModel,
    NoteIdentifiers,
    NoteLinks,
    NoteMetadata,
    NoteContent
    )

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
