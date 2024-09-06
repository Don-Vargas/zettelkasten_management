from src.utils.note_utils.search_note_utils import search_notes

def search_notes_action(address):
    keyword = input("Enter keyword to search in inbox: ")
    results = search_notes(keyword, address)
    print(f"Found {len(results)} notes:")
    for result in results:
        print(result)
