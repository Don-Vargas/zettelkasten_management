from datetime import datetime
from typing import List, Tuple

from src.utils.note_utils.note_model import (
    NoteModel,
    NoteIdentifiers,
    NoteLinks,
    NoteMetadata,
    NoteContent
)
from src.utils.note_utils.search_notes import list_all_titles
from .create_note import create_note
from .note_creation_utils import format_tags
from src import NOTES_DIR_PERMA, NOTES_DIR_INBOX

def title_check(title: str, titles_with_uuids: List[Tuple[str, str]]) -> bool:
    """
    Checks if a given title already exists in the list of titles with UUIDs.

    Parameters:
        title (str): The title to check.
        titles_with_uuids (list[tuple]): A list of tuples containing titles and their associated UUIDs.

    Returns:
        bool: True if the title already exists, otherwise False.
    """
    return any(t == title for t, _ in titles_with_uuids)

def new_note():
    """
    Orchestrates the process of creating a new note, including gathering user input and saving the note.
    """
    # Gather input for the new note
    title = input("Enter the title of the note: \n")
    titles_with_uuids = list_all_titles(NOTES_DIR_PERMA)
    
    # Ensure the title is unique
    while title_check(title, titles_with_uuids):
        existing_uuids = [uuid for t, uuid in titles_with_uuids if t == title]
        print(f"This title already exists in permanent notes with UUID(s): {', '.join(existing_uuids)}")
        title = input("Please enter a different note title \n")

    content = input("Enter the content of the note: \n")
    tags_input = input("Enter tags with the format '#tag' (comma-separated): \n")
    tags = format_tags(tags_input)
    references = input("Enter valid reference keys (comma-separated): \n").split(',')
    thoughts = input("Enter any additional thoughts: \n")

    # Create the NoteModel object
    new_note = NoteModel(
        identifiers=NoteIdentifiers(uuid=None, zk_uid=None),
        date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        metadata=NoteMetadata(references=references, tags=tags),
        links=NoteLinks(forward=[], backward=[]),
        contents=NoteContent(title=title, content=content, thoughts_connections=thoughts)
    )

    # Save the note using the create_note function
    create_note(new_note, NOTES_DIR_INBOX)
