import uuid
from src import UID_FORMAT

def generate_zk_uid() -> str:
    """
    TODO:
    Generates a unique Zettelkasten identifier (ZK_UID) based on the current timestamp.

    Returns:
        str: A string representing the unique Zettelkasten identifier.
    """
    return "None"

def generate_uuid() -> str:
    """
    Generates a unique UUID.

    Returns:
        str: A string representing the unique UUID.
    """
    return str(uuid.uuid4())

def format_tags(tags_input: str) -> list[str]:
    """
    Formats the tags input by ensuring each tag starts with a '#'.

    Parameters:
        tags_input (str): The tags input by the user, separated by commas.

    Returns:
        list[str]: A list of formatted tags.
    """
    tags = [tag.strip() for tag in tags_input.split(',')]
    formatted_tags = [tag if tag.startswith('#') else '#' + tag for tag in tags]
    return formatted_tags
