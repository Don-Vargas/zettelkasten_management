Outline for a Python script that can help you manage your notes inside the "notes" folder. This script will allow you to create, search, and link notes, all while adhering to the Zettelkasten methodology.


Inbox, this folder contains notes that are not linked yet or are missing a zk_uid
zk_uid shold be use to conect notes beside tags.

# Structured outline of the three-phase workflow

visualized in a clear diagram-like structure:

## Phase 1: Reference Box
### Goal: 
Collect references and create associated reference notes.

### Steps:
Create BibTeX Reference:

Add the source to your BibTeX database.
Generate a unique BibTeX key (e.g., author_year).
Create Reference Note:

Fields:
    - BibTeX Key: Ensure it matches the source.
    - Summary: Provide a concise overview of the source.
    - Bullet Points: Highlight key insights or takeaways.
    - Tags: Capture essential keywords or themes for quick reference.
    
### Outcome:
BibTeX reference and a reference note with all the critical information for later use.

## Phase 2: Inbox Workflow

### Goal: 
Capture ideas and content in raw, unprocessed form.

### Steps:
Create New Notes:

Fields:
Title: Give each note a descriptive title.
Content: Add the main body of the note.
Identifiers: Assign the note's UUID, date, and organic_zettelkasten_id.
BibTeX References: Link any relevant sources from the Reference Box using their BibTeX keys.
Tags: Manually assign tags (optional at this stage).

Verify Title Uniqueness:
Ensure that the note's title is unique in the system.

### Outcome:
A collection of raw notes with identifiers and any relevant references, ready for further refinement.

## Phase 3: Permanent Box
### Goal: 
Finalize notes, ensure completeness, and establish cross-references.

### Steps:
1. Verify Note Completeness:

2. Ensure all notes include:
Title (verified to be unique).
Content (refined and complete).
Tags (can be automatically generated or manually added).
Cross-references (forward and backward).
3. Add Cross-References:

Forward References: Add references to other notes linked from the current note.
Backward References: Track any notes that reference this current note.
Tag Refinement:

Ensure the tags cover all essential themes and concepts in the note.
Add any missing tags or auto-generate them based on content.
### Outcome:
Fully refined, interconnected notes with all necessary metadata, tags, and cross-references.


## Diagram

```
Phase 1: Reference Box
    ↓
    - Create BibTeX reference
    - Create reference note with 
        + BibTeX key, 
        + summary, 
        + bullet points, and 
        + tags

Phase 2: Inbox Workflow
    ↓
    - Create notes with 
        + title, 
        + content, 
        + IDs, 
        + BibTeX references, and 
        + tags
    - Verify title uniqueness

Phase 3: Permanent Box
    ↓
    - Verify completeness of notes (title, content, tags, cross-references)
    - Add forward and backward references
    - Finalize and refine tags
```
