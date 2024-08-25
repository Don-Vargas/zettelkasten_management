"""
note_model.py
------------

This module defines the data models for representing and managing notes in a Zettelkasten system.

Classes:
- NoteIdentifiers: Represents unique identifiers for a note.
- NoteLinks: Manages forward and backward links associated with a note.
- NoteMetadata: Contains metadata such as references and tags for a note.
- NoteContent: Holds the title, main content, and additional thoughts of a note.
- NoteModel: The main class combining all components to represent a complete note.

Key Features:
- Creates and manages notes with various attributes, including identifiers, metadata, links, 
    and content.
- Provides methods for adding references, tags, and links, and updating thoughts/connections.

Usage:
- Instantiate the NoteModel class with appropriate attributes to create a note.
- Utilize methods to modify and manage note attributes.

Dependencies:
- Imports datetime for handling date and time.
- Imports List, Dict, Optional from typing for type annotations.
- Imports field, dataclass from dataclasses for defining data classes.

Author:
Hector Alejandro Vargas Gutierrez

License:
[Specify the license under which the module is distributed, if applicable.]
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime

@dataclass
class NoteIdentifiers:
    """
    Represents the identifiers for a note.

    Attributes:
        uuid (str): The universally unique identifier for the note.
        zk_uid (str): The unique Zettelkasten identifier for the note.
    """
    uuid: str
    zk_uid: str

@dataclass
class NoteLinks:
    """
    Manages the links associated with a note.

    Attributes:
        forward (List[Dict[str, str]]): A list of dictionaries representing forward links 
        to other notes.
        backward (List[Dict[str, str]]): A list of dictionaries representing backward links from 
        other notes.
    """
    forward: List[Dict[str, str]] = field(default_factory=list)
    backward: List[Dict[str, str]] = field(default_factory=list)

@dataclass
class NoteMetadata:
    """
    Contains metadata related to the note.

    Attributes:
        references (List[str]): A list of references related to the note.
        tags (List[str]): A list of tags associated with the note.
    """
    references: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

@dataclass
class NoteContent:
    """
    Contains the content and additional thoughts of the note.

    Attributes:
        title (str): The title of the note.
        content (str): The main content of the note.
        thoughts_connections (Optional[str]): Additional thoughts or connections related 
        to the note.
    """
    title: str = ""
    content: str = ""
    thoughts_connections: Optional[str] = None

@dataclass
class NoteModel:
    """
    Represents a complete note with all its attributes.

    Attributes:
        identifiers (NoteIdentifiers): The identifiers for the note (UUID and Zettelkasten UID).
        date (str): The date when the note was created, in 'YYYY-MM-DD HH:MM:SS' format. 
                Default is the current date.
        metadata (NoteMetadata): Metadata related to the note, including references and tags.
        links (NoteLinks): Links associated with the note, including forward and backward links.
        contents (NoteContent): The content of the note, including title, main content, 
        and additional thoughts.
    """

    identifiers: NoteIdentifiers
    date: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    metadata: NoteMetadata = field(default_factory=NoteMetadata)
    links: NoteLinks = field(default_factory=NoteLinks)
    contents: NoteContent = field(default_factory=NoteContent)

    def __str__(self):
        """
        Return a string representation of the note.
        """
        note_str = f"UUID: {self.identifiers.uuid}\n"
        note_str += f"Title: {self.contents.title}\n"
        note_str += f"ZK_UID: {self.identifiers.zk_uid}\n"
        note_str += f"Date: {self.date}\n"
        note_str += f"Content:\n{self.contents.content}\n"
        if self.metadata.references:
            note_str += f"References:\n{', '.join(self.metadata.references)}\n"
        note_str += f"Tags: {', '.join(self.metadata.tags)}\n" if self.metadata.tags else ""
        if self.links.forward:
            note_str += "Links Forward to Other Notes:\n"
            for link in self.links.forward:
                note_str += f"Related to: ZK_UID {link['ZK_UID']} ({link['Description']})\n"
        if self.links.backward:
            note_str += "Linked Backward from Other Notes:\n"
            for link in self.links.backward:
                note_str += f"Related to: ZK_UID {link['ZK_UID']} ({link['Description']})\n"
        if self.contents.thoughts_connections:
            note_str += f"Thoughts/Connections:\n{self.contents.thoughts_connections}\n"

        return note_str

    def add_reference(self, reference: str):
        """
        Add a reference to the note.

        Args:
            reference (str): The reference to add.
        """
        self.metadata.references.append(reference)

    def add_tag(self, tag: str):
        """
        Add a tag to the note.

        Args:
            tag (str): The tag to add.
        """
        self.metadata.tags.append(tag)

    def add_forward_link(self, zk_uid: str, description: str):
        """
        Add a forward link to another note.

        Args:
            zk_uid (str): The ZK_UID of the related note.
            description (str): A description of the relationship.
        """
        self.links.forward.append({'ZK_UID': zk_uid, 'Description': description})

    def add_backward_link(self, zk_uid: str, description: str):
        """
        Add a backward link from another note.

        Args:
            zk_uid (str): The ZK_UID of the related note.
            description (str): A description of the relationship.
        """
        self.links.backward.append({'ZK_UID': zk_uid, 'Description': description})

    def set_thoughts_connections(self, thoughts: str):
        """
        Set or update the thoughts/connections for the note.

        Args:
            thoughts (str): The thoughts or connections to set.
        """
        self.contents.thoughts_connections = thoughts
