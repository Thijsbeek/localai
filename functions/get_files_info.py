import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct the target directory path
        target_dir = os.path.normpath(
            os.path.join(working_dir_abs, directory)
        )

        # Check whether the target directory is within the working directory
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir])
            == working_dir_abs
        )

        if not valid_target_dir:
            return (
                f'Error: Cannot list "{directory}" '
                'as it is outside the permitted working directory'
            )

        # Check whether the target path is a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # return f'Success: "{directory}" is within the working directory'

    # Get the items in the target directory
        items = os.listdir(target_dir)

        # Build the output string
        result = ""

        for item in items:
            item_path = os.path.join(target_dir, item)

            file_size = os.path.getsize(item_path)
            is_directory = os.path.isdir(item_path)

            result += (
                f"- {item}: file_size={file_size} bytes, "
                f"is_dir={is_directory}\n"
            )

        return result

    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}