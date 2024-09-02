"""
Zettelkasten Note Manager CLI Module

This module provides a command-line interface (CLI) for managing notes in a Zettelkasten system. 
The Zettelkasten method is a note-taking and knowledge management system that helps in organizing 
information in a network of interconnected notes. This CLI allows users to create, search, list, 
and link notes within the system.

Classes:
    NoteModel: Represents the structure of a note, including metadata, content, and links.
    NoteIdentifiers: Contains unique identifiers for notes, such as UUID and ZK UID.
    NoteLinks: Manages forward and backward links between notes.
    NoteMetadata: Stores metadata for notes, including references and tags.
    NoteContent: Holds the main content of the note, including title, content, and thoughts.

Functions:
    main(): The entry point of the CLI, providing a menu for the user to interact with the system.
    create_new_note(): Handles the creation of a new note by gathering user input.
    search_notes_in_inbox(): Searches for notes in the inbox directory based on user input.
    search_notes_in_permanent(): Searches for notes in the permanent notes directory based on 
                                    user input.
    list_inbox_notes(): Lists all notes in the inbox directory.
    list_permanent_notes(): Lists all notes in the permanent notes directory.
    link_notes_action(): Manages the linking of notes based on user input.

Usage:
    Run this module as a script to start the Zettelkasten Note Manager CLI. The user will be 
    presented with a menu of options to create, search, list, or link notes.

Dependencies:
    - os: For file and directory operations.
    - datetime: For handling date and time operations.
    - note_model: For managing the structure and content of notes.

Author:
    [Your Name]

License:
    [Your License Information]
"""
import os
import datetime
from typing import List, Tuple

from src.utils.note_model import NoteModel, NoteIdentifiers, NoteLinks, NoteMetadata, NoteContent
from src.inbox_.create_note import create_note
from src.utils.search_notes import search_notes, list_all_titles
from src.inbox_.link_notes import link_forward_notes
from src.utils.list_all_notes import list_all_notes
from src import NOTES_DIR_INBOX
from src import NOTES_DIR_PERMA


def title_check(title: str, titles_with_uuids: List[Tuple[str, str]]) -> bool:
    """
    Checks if the title is repeated in the list of titles with their corresponding UUIDs.

    Parameters:
        title (str): The title to check.
        titles_with_uuids (List[Tuple[str, str]]): A list of tuples, where each tuple contains
        a title and its corresponding UUID.

    Returns:
        bool: True if the title is repeated, False otherwise.
    """
    # Count the number of occurrences of the title in the list
    occurrences = sum(1 for t, _ in titles_with_uuids if t == title)

    # If the title occurs more than once, it's repeated
    return occurrences > 0

def format_tags(tags_input: str) -> List[str]:
    """
    Formats tags to ensure each tag starts with a '#' character.

    Parameters:
        tags_input (str): A comma-separated string of tags.

    Returns:
        List[str]: A list of formatted tags where each tag starts with '#'.
    """
    # Split the input string into a list of tags
    tags = [tag.strip() for tag in tags_input.split(',')]

    # Format each tag to ensure it starts with '#'
    formatted_tags = [tag if tag.startswith('#') else '#' + tag for tag in tags]

    return formatted_tags

def create_new_note():
    """Handles the creation of a new note."""
    title = input("Enter the title of the note: \n")

    # Get all titles with their UUIDs
    titles_with_uuids = list_all_titles(NOTES_DIR_PERMA)
    # Check if the title is already in the list and prompt the user to enter a different title
    while title_check(title, titles_with_uuids):
        # Find and display the UUIDs for the existing title
        existing_uuids = [uuid for t, uuid in titles_with_uuids if t == title]
        print(f"This title already exists in permanent notes with UUID(s): {', '.join(existing_uuids)}")
        title = input("Please enter a different note title \n")

    print("\n...................................\n ")
    content = input("Enter the content of the note: \n")
    print("\n...................................\n ")
    tags_input = input("Enter tags with the format '#tag' (comma-separated): \n")
    tags = format_tags(tags_input)
    print("\n...................................\n ")
    references = input("Enter valid reference keys (comma-separated): \n").split(',')

    '''
    TODO:
    - verificar si las referencias existen en el jabref.
    '''

    print("\n...................................\n ")
    thoughts = input("Enter any additional thoughts: \n")
    print("\n...................................\n ")

    new_note = NoteModel(
        identifiers=NoteIdentifiers(
            uuid=None,
            zk_uid=None
        ),
        date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        metadata=NoteMetadata(
            references=references,
            tags=tags
        ),
        links=NoteLinks(
            forward=[],
            backward=[]
        ),
        contents=NoteContent(
            title=title,
            content=content,
            thoughts_connections=thoughts
        )
    )

    create_note(new_note)
    print("Note created successfully.")

def search_notes_in_inbox():
    """Searches notes in the inbox directory."""
    keyword = input("Enter keyword to search in inbox: ")
    results = search_notes(keyword, NOTES_DIR_INBOX)
    print(f"Found {len(results)} notes:")
    for result in results:
        print(result)


def list_inbox_notes():
    """Lists all notes in the inbox directory."""
    notes = list_all_notes(NOTES_DIR_INBOX)
    print(f"Total notes: {len(notes)}")
    for note in notes:
        print(note)
        
def link_notes_action():
    """Handles linking notes."""
    '''
    note_uid = input("Enter the UID of the note to link from: ")
    
    uids_input = input("Enter the UIDs of the notes to link to (comma-separated): ")
    linked_uids = uids_input.split(',')
    link_forward_notes(note_uid, linked_uids, NOTES_DIR_PERMA)
    TODO:
    cambiar approach.
    
    '''
    print("Notes linked successfully.")
    
def exit_program():
    """Exits the program."""
    print("Exiting the program.")
    exit()

def inbox_menu_():
    """
    Main function for the Zettelkasten Note Manager command-line interface.
    """
    options = {
        '1': create_new_note,
        '2': search_notes_in_inbox,
        '3': list_inbox_notes,
        '4': link_notes_action,
        '5': lambda: 'main',
        '6': exit_program,
    }

    while True:
        print("\n____________________________________\n ")
        print("Zettelkasten Note Manager \n")
        print("Welcome to Inbox Notes.")
        print("\n____________________________________\n ")
        print("1. Create a new note")
        print("2. Search notes in inbox")
        print("3. List all inbox notes")
        print("4. Link notes")
        print("5. Exit to main menu.")
        print("6. Exit")
        print("\n____________________________________\n ")

        choice = input("Enter your choice: ")
        print("\n____________________________________\n ")

        # Execute the corresponding function, or print an error message if invalid
        action = options.get(choice, lambda: print("Invalid choice. Please try again."))()
        if action:
            return action  # Return to the main loop for processing
