from src.inbox_notes_.link_notes_utils.link_notes import link_note_forward

from src import NOTES_DIR_INBOX, NOTES_DIR_PERMA

'''
TODO:
    trabajar en este linkage.
'''

def link_notes_action():
    note_uid1 = input("Enter The ZK_UID of the note to which forward links will be added: \n")

    #linked_uids = input("Enter The ZK_UID of the note to which forward links will be added: \n")

    #directories = input("Enter The ZK_UID of the note to which forward links will be added: \n")
    
    linked_uids = [
        {'ZK_UID':'ZK_UID 20240822-003', 'Description': 'Benefits of Morning Routines'},
        {'ZK_UID':'ZK_UID 20240822-004', 'Description': 'Benefits of Nigth Routines'}
    ]

    directories = [NOTES_DIR_INBOX, NOTES_DIR_PERMA]

    link_note_forward(note_uid1, linked_uids, directories)
    print("Notes linked successfully.")
