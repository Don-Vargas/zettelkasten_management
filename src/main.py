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
import os  # Import the os module for file and directory operations
import datetime

# Import functions from the same src/ folder
from . note_model import NoteModel, NoteIdentifiers, NoteLinks, NoteMetadata, NoteContent
from . create_note import create_note
from . search_notes import search_notes
from . link_notes import link_forward_notes
from . list_all_notes import list_all_notes
from . import NOTES_DIR_INBOX  # Directory where all the notes are stored
from . import NOTES_DIR_PERMA  # Directory where all the notes are stored

def create_new_note():
    """Handles the creation of a new note."""
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    references = input("Enter references (comma-separated): ").split(',')
    thoughts = input("Enter any additional thoughts: ")

    # Create an instance of NoteModel
    new_note = NoteModel(
        identifiers=NoteIdentifiers(
            uuid=None,
            zk_uid=None
        ),
        # You can set a specific date below if needed
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

    # Call the create_note function with the note instance
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

def main():
    """
    Main function for the Zettelkasten Note Manager command-line interface.
    """
    while True:
        # Display the main menu
        print("Zettelkasten Note Manager")
        print("1. Create a new note")
        print("2. Search notes in inbox")
        print("3. Search notes in permanent notes")
        print("4. List all inbox notes")
        print("5. List all permanent notes")
        print("6. Link notes")
        print("7. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Handle user choices
        if choice == '1':
            create_new_note()
        elif choice == '2':
            search_notes_in_inbox()
        elif choice == '3':
            search_notes_in_permanent()
        elif choice == '4':
            list_inbox_notes()
        elif choice == '5':
            list_permanent_notes()
        elif choice == '6':
            link_notes_action()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Ensure the notes directory exists
    os.makedirs(NOTES_DIR_INBOX, exist_ok=True)
    os.makedirs(NOTES_DIR_PERMA, exist_ok=True)

    # Start the main function
    main()
