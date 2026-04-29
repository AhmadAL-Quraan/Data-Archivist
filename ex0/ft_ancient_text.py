import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        exit(0)
    print("=== Cyber Archives Recovery ===")

    try:
        print(f"Accessing file {sys.argv[1]}")
        file_open: typing.IO = open(sys.argv[1], "r")
        print(file_open.read())
        file_open.close()
        print(f"File ’{sys.argv[1]}’ closed.")

    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
