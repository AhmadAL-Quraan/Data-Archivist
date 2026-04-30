import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        exit(0)
    print("=== Cyber Archives Recovery & Preservation ===")

    try:
        print(f"Accessing file {sys.argv[1]}")
        file_open: typing.IO = open(sys.argv[1], "r")
        print("---")
        content: str = file_open.read()
        print(content, end="")
        print("---")
        file_open.close()
        print(f"File '{sys.argv[1]}' closed.\n")
        print("\nTransform data:\n---")
        List_after: str = ""
        save: str = ""
        inte: int = 0
        for i in content:
            if i == "\n":
                List_after += save
                List_after += "#"
                save = ""
            save += i

        print(f"{List_after}\n---")
        print("Enter new file name (or empty): ")

        inp: str = sys.stdin.readline().rstrip().strip()
        if not inp:
            sys.stdout.write("Not saving data")
        else:
            new_file = open(inp, "w")
            print(f"Saving data to '{inp}'")
            new_file.write(List_after)
            print(f"Data saved in file '{inp}'.")
            new_file.close()
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
            file=sys.stderr,
        )
