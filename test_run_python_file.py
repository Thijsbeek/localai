
from functions.run_python_file import run_python_file


def main():
    print("Result 1:")
    print(run_python_file("calculator", "main.py"))

    print("\nResult 2:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\nResult 3:")
    print(run_python_file("calculator", "tests.py"))

    print("\nResult 4:")
    print(run_python_file("calculator", "../main.py"))

    print("\nResult 5:")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\nResult 6:")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
