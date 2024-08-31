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

from src.note_model import NoteModel, NoteIdentifiers, NoteLinks, NoteMetadata, NoteContent
from src.create_note import create_note
from src.search_notes import search_notes
from src.link_notes import link_forward_notes
from src.list_all_notes import list_all_notes
from src import NOTES_DIR_INBOX
from src import NOTES_DIR_PERMA

def create_new_note():
    """Handles the creation of a new note."""
    title = input("Enter the title of the note: \n")
    content = input("Enter the content of the note: \n")
    tags = input("Enter tags (comma-separated): \n").split(',')
    references = input("Enter references (comma-separated): \n").split(',')
    thoughts = input("Enter any additional thoughts: \n")

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

def search_notes_in_permanent():
    """Searches notes in the permanent notes directory."""
    keyword = input("Enter keyword to search in permanent notes: ")
    results = search_notes(keyword, NOTES_DIR_PERMA)
    print(f"Found {len(results)} notes:")
    for result in results:
        print(result)

def list_inbox_notes():
    """Lists all notes in the inbox directory."""
    notes = list_all_notes(NOTES_DIR_INBOX)
    print(f"Total notes: {len(notes)}")
    for note in notes:
        print(note)

def list_permanent_notes():
    """Lists all notes in the permanent notes directory."""
    notes = list_all_notes(NOTES_DIR_PERMA)
    print(f"Total notes: {len(notes)}")
    for note in notes:
        print(note)

def link_notes_action():
    """Handles linking notes."""
    note_uid = input("Enter the UID of the note to link from: ")
    uids_input = input("Enter the UIDs of the notes to link to (comma-separated): ")
    linked_uids = uids_input.split(',')
    link_forward_notes(note_uid, linked_uids, NOTES_DIR_PERMA)
    print("Notes linked successfully.")

def exit_program():
    """Exits the program."""
    print("Exiting the program.")
    exit()

def main():
    """
    Main function for the Zettelkasten Note Manager command-line interface.
    """
    options = {
        '1': create_new_note,
        '2': search_notes_in_inbox,
        '3': search_notes_in_permanent,
        '4': list_inbox_notes,
        '5': list_permanent_notes,
        '6': link_notes_action,
        '7': exit_program,
    }

    while True:
        print("Zettelkasten Note Manager")
        print("1. Create a new note")
        print("2. Search notes in inbox")
        print("3. Search notes in permanent notes")
        print("4. List all inbox notes")
        print("5. List all permanent notes")
        print("6. Link notes")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # Execute the corresponding function, or print an error message if invalid
        options.get(choice, lambda: print("Invalid choice. Please try again."))()

if __name__ == "__main__":
    os.makedirs(NOTES_DIR_INBOX, exist_ok=True)
    os.makedirs(NOTES_DIR_PERMA, exist_ok=True)
    main()
