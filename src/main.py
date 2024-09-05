# main.py
from src.inbox_notes_ import inbox_menu_
from src.permanent_notes_ import permanent_notes_menu_
from src.reference_notes_ import reference_notes_menu_
from src.utils.menu_utils import exit_program

def main():
    """
    Main function for the Zettelkasten Note Manager command-line interface.
    """
    options = {
        '1': inbox_menu_,
        '2': permanent_notes_menu_,
        '3': reference_notes_menu_,
        '4': exit_program,
    }

    while True:
        print("\n____________________________________\n ")
        print("Zettelkasten Note Manager")
        print("\n____________________________________\n ")
        print("1. Inbox Menu")
        print("2. Permanent Notes Menu")
        print("3. Reference Notes Menu")
        print("4. Exit")
        print("\n____________________________________\n ")

        choice = input("Enter your choice: ")
        print("\n____________________________________\n ")

        # Execute the corresponding function, or print an error message if invalid
        action = options.get(choice, lambda: print("Invalid choice. Please try again."))()

        # Check the returned action and handle it
        if action == 'main':
            continue  # Go back to the main menu
        elif action is None:
            break  # Exit the program
        else:
            print("Invalid action or error.")
            break

if __name__ == "__main__":
    main()
