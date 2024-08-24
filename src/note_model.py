from datetime import datetime

class NoteModel:
    def __init__(self, uuid, title, zk_uid, content, date=None, references=None, tags=None, 
                 links_forward_to_other_notes=None, linked_backward_from_other_notes=None, 
                 thoughts_connections=None):
        """
        Initialize a new NoteModel instance.

        Args:
            uuid (str): The universally unique identifier for the note.
            title (str): The title of the note.
            zk_uid (str): The unique Zettelkasten identifier for the note.
            content (str): The main content of the note.
            date (str, optional): The date when the note was created, in full date format. Default is the current date.
            references (str or list of str, optional): References related to the note. Default is None.
            tags (list of str, optional): Tags associated with the note. Default is None.
            links_forward_to_other_notes (list of dict, optional): Links to other notes in the form of {'ZK_UID': 'Description'} pairs. Default is None.
            linked_backward_from_other_notes (list of dict, optional): Links from other notes in the form of {'ZK_UID': 'Description'} pairs. Default is None.
            thoughts_connections (str, optional): Additional thoughts or connections. Default is None.
        """
        self.uuid = uuid
        self.title = title
        self.zk_uid = zk_uid
        self.content = content
        self.date = date if date else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.references = references if references else []
        self.tags = tags if tags else []
        self.links_forward_to_other_notes = links_forward_to_other_notes if links_forward_to_other_notes else []
        self.linked_backward_from_other_notes = linked_backward_from_other_notes if linked_backward_from_other_notes else []
        self.thoughts_connections = thoughts_connections

    def __str__(self):
        """
        Return a string representation of the note.
        """
        note_str = f"UUID: {self.uuid}\n"
        note_str += f"Title: {self.title}\n"
        note_str += f"ZK_UID: {self.zk_uid}\n"
        note_str += f"Date: {self.date}\n"
        note_str += f"Content:\n{self.content}\n"
        note_str += f"References:\n{', '.join(self.references)}\n" if self.references else ""
        note_str += f"Tags: {', '.join(self.tags)}\n" if self.tags else ""
        if self.links_forward_to_other_notes:
            note_str += "Links Forward to Other Notes:\n"
            for link in self.links_forward_to_other_notes:
                note_str += f"Related to: ZK_UID {link['ZK_UID']} ({link['Description']})\n"
        if self.linked_backward_from_other_notes:
            note_str += "Linked Backward from Other Notes:\n"
            for link in self.linked_backward_from_other_notes:
                note_str += f"Related to: ZK_UID {link['ZK_UID']} ({link['Description']})\n"
        note_str += f"Thoughts/Connections:\n{self.thoughts_connections}\n" if self.thoughts_connections else ""
        return note_str

    def add_reference(self, reference):
        """
        Add a reference to the note.

        Args:
            reference (str): The reference to add.
        """
        self.references.append(reference)

    def add_tag(self, tag):
        """
        Add a tag to the note.

        Args:
            tag (str): The tag to add.
        """
        self.tags.append(tag)

    def add_forward_link(self, zk_uid, description):
        """
        Add a forward link to another note.

        Args:
            zk_uid (str): The ZK_UID of the related note.
            description (str): A description of the relationship.
        """
        self.links_forward_to_other_notes.append({'ZK_UID': zk_uid, 'Description': description})

    def add_backward_link(self, zk_uid, description):
        """
        Add a backward link from another note.

        Args:
            zk_uid (str): The ZK_UID of the related note.
            description (str): A description of the relationship.
        """
        self.linked_backward_from_other_notes.append({'ZK_UID': zk_uid, 'Description': description})

    def set_thoughts_connections(self, thoughts):
        """
        Set or update the thoughts/connections for the note.

        Args:
            thoughts (str): The thoughts or connections to set.
        """
        self.thoughts_connections = thoughts
