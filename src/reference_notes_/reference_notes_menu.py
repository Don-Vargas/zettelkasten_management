import os

from src.utils.menu_utils import welcome_note
from src import NOTES_DIR_REFERENCE

entorno = 'R E F E R E N C E'

def exit_program():
    """Exits the program."""
    print("Exiting the program.")
    exit()

def reference_notes_menu_():
    """
    permanent_notes_menu function for the Zettelkasten Note Manager command-line interface.
    """    
    options = {
        '0': lambda: welcome_note(entorno),
        '2': lambda: 'main',
        '3': exit_program,
    }

    while True:
        print("\n____________________________________\n ")
        print("Zettelkasten Note Manager \n")
        print("Welcome to Reference Notes.")
        print("\n____________________________________\n ")
        print("0. welcome note")
        print("2. Exit to main menu.")
        print("3. Exit")
        print("\n____________________________________\n ")

        choice = input("Enter your choice: ")
        print("\n____________________________________\n ")

        # Execute the corresponding function, or print an error message if invalid
        action = options.get(choice, lambda: print("Invalid choice. Please try again."))()
        if action:
            return action  # Return to the main loop for processing
