import os  # Import the os module for file and directory operations

# Import functions from the same src/ folder
from . import create_note, search_notes, list_all_notes, link_notes
from . import NOTES_DIR  # Directory where all the notes are stored

def main():
    """
    Main function for the Zettelkasten Note Manager command-line interface.

    This function presents a menu to the user, allowing them to create notes, search notes,
    list all notes, link notes, or exit the program. It processes user input to perform
    the chosen actions.

    Returns:
        None
    """
    while True:
        # Display the main menu
        print("Zettelkasten Note Manager")
        print("1. Create a new note")
        print("2. Search notes")
        print("3. List all notes")
        print("4. Link notes")
        print("5. Exit")
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        # Handle user choices
        if choice == '1':
            # Create a new note
            title = input("Enter the title of the note: ")
            content = input("Enter the content of the note: ")
            tags = input("Enter tags (comma-separated): ").split(',')
            references = input("Enter references (comma-separated): ")
            thoughts = input("Enter any additional thoughts: ")
            create_note(title, content, tags, references, None, thoughts)
            print("Note created successfully.")
        elif choice == '2':
            # Search notes
            keyword = input("Enter keyword to search: ")
            results = search_notes(keyword)
            print(f"Found {len(results)} notes:")
            for result in results:
                print(result)
        elif choice == '3':
            # List all notes
            notes = list_all_notes()
            print(f"Total notes: {len(notes)}")
            for note in notes:
                print(note)
        elif choice == '4':
            # Link notes
            note_uid = input("Enter the UID of the note to link from: ")
            linked_uids = input("Enter the UIDs of the notes to link to (comma-separated): ").split(',')
            link_notes(note_uid, linked_uids)
            print("Notes linked successfully.")
        elif choice == '5':
            # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Ensure the notes directory exists
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
    
    # Start the main function
    main()
