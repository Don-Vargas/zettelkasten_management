from src.utils.note_utils.list_all_notes import list_all_notes
from src import NOTES_DIR_INBOX

def list_inbox_notes():
    notes = list_all_notes(NOTES_DIR_INBOX)
    print(f"Total notes: {len(notes)}")
    for note in notes:
        print(note)
