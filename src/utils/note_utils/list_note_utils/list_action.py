from src.utils.note_utils.list_note_utils.list_notes import list_notes

def list_notes_action(address):
    notes = list_notes(address)
    print(f"Total notes: {len(notes)}")
    for note in notes:
        print(note)
