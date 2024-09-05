from src.utils.note_utils.search_notes import search_notes
from src import NOTES_DIR_INBOX

def search_notes_in_inbox():
    keyword = input("Enter keyword to search in inbox: ")
    results = search_notes(keyword, NOTES_DIR_INBOX)
    print(f"Found {len(results)} notes:")
    for result in results:
        print(result)
