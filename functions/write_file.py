import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct the target file path
        target_file = os.path.normpath(
            os.path.join(working_dir_abs, file_path)
        )

        # Check whether the target file is within the working directory
        valid_target_file = (
            os.path.commonpath([working_dir_abs, target_file])
            == working_dir_abs
        )

        if not valid_target_file:
            return (
                f'Error: Cannot write to "{file_path}" '
                'as it is outside the permitted working directory'
            )

        # Check whether the target path is a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Create parent directories if they don't exist
        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)

        # Write content to the file
        with open(target_file, "w") as file:
            file.write(content)

        return (
            f'Successfully wrote to "{file_path}" '
            f'({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"