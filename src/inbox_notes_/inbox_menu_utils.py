import os
from datetime import datetime
from src import UID_FORMAT

def ensure_uuid_and_date(address: str):
    """
    Check all .txt files in the given directory, verify if the "UUID:" and "Date:" fields
    are populated, and populate them if they are missing.

    Args:
        address (str): The directory address where .txt files are located.
    """
    # Iterate over all files in the directory
    for filename in os.listdir(address):
        if filename.endswith('.txt'):
            file_path = os.path.join(address, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Initialize flags and store index of UUID and Date
            has_uuid = False
            has_date = False
            uuid_index = None
            date_index = None

            # Check if UUID and Date are present
            for i, line in enumerate(lines):
                if line.startswith("UUID:"):
                    has_uuid = bool(line.split("UUID:")[1].strip())
                    uuid_index = i
                elif line.startswith("Date:"):
                    has_date = bool(line.split("Date:")[1].strip())
                    date_index = i

            # Generate missing UUID and Date
            updated = False
            if not has_uuid:
                generated_uuid = generate_uuid()
                if uuid_index is not None:
                    lines[uuid_index] = f"UUID: {generated_uuid}\n"
                else:
                    lines.insert(0, f"UUID: {generated_uuid}\n")
                updated = True

            if not has_date:
                generated_date = datetime.now().strftime(UID_FORMAT)
                if date_index is not None:
                    lines[date_index] = f"Date: {generated_date}\n"
                else:
                    # Find where to insert the date if not present
                    if uuid_index is not None:
                        lines.insert(uuid_index + 1, f"Date: {generated_date}\n")
                    else:
                        lines.insert(1, f"Date: {generated_date}\n")
                updated = True

            # Write back to the file if updates were made
            if updated:
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                print(f"Updated file: {filename}")