import os
import subprocess
import sys

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
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
                        f'Error: Cannot execute "{file_path}" '
                        'as it is outside the permitted working directory'
                    )

                # Check whether the target file path points to a file
                if not os.path.isfile(target_dir):
                    return f'Error: "{file_path}" does not exist or is not a regular file'

                if not file_path.endswith(".py"):
                    return f'Error: "{file_path}" is not a Python file'

                # Prepare the command to run the Python file
                command = ["python", target_dir]

                if args:
                    command.extend(args)

                # Execute the Python file
                result = subprocess.run(
                    command,
                    cwd=working_dir_abs,
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                # Build the output string
                output = []

                if result.returncode != 0:
                    output.append(f"Process exited with code {result.returncode}")

                if not result.stdout and not result.stderr:
                    output.append("No output produced")
                else:
                    if result.stdout:
                        output.append(f"STDOUT:\n{result.stdout}")
                    if result.stderr:
                        output.append(f"STDERR:\n{result.stderr}")

                return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute a Python file with optional command-line arguments.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the Python file to execute."
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional command-line arguments to pass to the Python file."
                }
            },
            "required": ["file_path"]
        }
    }
}