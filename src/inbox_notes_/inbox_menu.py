from src.utils.menu_utils import welcome_note
from src.inbox_notes_.note_creation import new_note
from .search_action import search_notes_in_inbox
from .list_action import list_inbox_notes
from .link_action import link_notes_action
from src.utils.menu_utils import exit_program

entorno = 'I N B O X'

def inbox_menu_():
    """
    Main function for the Zettelkasten Note Manager command-line interface.
    """
    options = {
        '0': lambda: welcome_note(entorno),
        '1': new_note,
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
        print("0. welcome note")
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
