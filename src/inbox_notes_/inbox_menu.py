from src.utils.menu_utils import welcome_note
from src.inbox_notes_.new_note_utils import new_note_action
from src.utils.note_utils.search_note_utils import search_notes_action
from src.utils.note_utils.list_note_utils import list_notes_action
from src.inbox_notes_.link_notes_utils import link_notes_action
from src.inbox_notes_.inbox_menu_utils import ensure_uuid_and_date
from src.utils.menu_utils import exit_program
from src import NOTES_DIR_INBOX

entorno = 'I N B O X'

def inbox_menu_():
    """
    Main function for the Zettelkasten Note Manager command-line interface.
    """
    options = {
        '0': lambda: welcome_note(entorno),
        '1': new_note_action,
        '2': lambda: search_notes_action(NOTES_DIR_INBOX),
        '3': lambda: list_notes_action(NOTES_DIR_INBOX),
        '4': link_notes_action,
        '5': lambda: 'main',
        '6': exit_program,
    }

    ensure_uuid_and_date(NOTES_DIR_INBOX)

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
