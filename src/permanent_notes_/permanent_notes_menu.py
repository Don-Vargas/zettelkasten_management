import os

from src import NOTES_DIR_INBOX
from src import NOTES_DIR_PERMA

def inbox_ingest():
    '''
    TODO:
    - validar que todas las notas de inbox tengan todos los campos completos.
    - cambiarle el nombre a los archivos de las notas.
    - sugerir notas que sean similares para elegir un buen ZK_UID
    - crear o validar que el ZK_UID no se repita.
    - cambiar las notas de inbox a permenent.
    '''
    pass

def welcome_note():
    """Welcome to the program."""
    print("Welcome to Permanent notes.")

def exit_program():
    """Exits the program."""
    print("Exiting the program.")
    exit()

def permanent_notes_menu_():
    """
    permanent_notes_menu function for the Zettelkasten Note Manager command-line interface.
    """
    print("Welcome to Permanent notes.")
    
    options = {
        '1': welcome_note,
        '2': lambda: 'main',
        '3': exit_program,
    }

    while True:
        print("\n____________________________________\n ")
        print("Zettelkasten Note Manager \n")
        print("Welcome to Permanent Notes.")
        print("\n____________________________________\n ")
        print("1. welcome note")
        print("2. Exit to main menu.")
        print("3. Exit")
        print("\n____________________________________\n ")

        choice = input("Enter your choice: ")
        print("\n____________________________________\n ")

        # Execute the corresponding function, or print an error message if invalid
        action = options.get(choice, lambda: print("Invalid choice. Please try again."))()
        if action:
            return action  # Return to the main loop for processing
