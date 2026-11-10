import os
from config import max_characters_file_content as max_chars

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
            # Get the absolute path of the working directory
            working_dir_abs = os.path.abspath(working_directory)
    
            # Construct the target directory path
            target_dir = os.path.normpath(
                os.path.join(working_dir_abs, file_path)
            )
    
            # Check whether the target directory is within the working directory
            valid_target_dir = (
                os.path.commonpath([working_dir_abs, target_dir])
                == working_dir_abs
            )
    
            if not valid_target_dir:
                return (
                    f'Error: Cannot read "{file_path}" '
                    'as it is outside the permitted working directory'
                )
    
            # Check whether the target file path points to a file
            if not os.path.isfile(target_dir):
                return f'Error: File not found or is not a regular file: "{file_path}"'

            with open(target_dir, "r", encoding="utf-8") as f:
                content = f.read(max_chars)

                # Check whether the file contains more content
                if f.read(1):
                    content += (
                        f'\n[...File "{file_path}" truncated at '
                        f'{max_chars} characters]'
                    )

            return content

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read the contents of a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file whose contents should be read."
                }
            },
            "required": ["file_path"]
        }
    }
} 