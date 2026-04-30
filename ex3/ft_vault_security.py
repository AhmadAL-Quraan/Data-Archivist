def secure_archive(
    file_name: str, mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    try:
        with open(file_name, mode) as file:
            if mode == "r":
                full_content: str = ""
                for i in file.read():
                    full_content += i

                return (True, full_content)
            elif mode == "w":
                file.write(content)
                return (True, "Content successfully written to file")
    except Exception as e:
        return (False, f"{e}")
    return (True, "Finished")


if __name__ == "__main__":
    tup = secure_archive("./text.txt")
    print("=== Cyber Archives Security ===\n")
    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("nonexistentfile"))
    print()
    print("Using ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("/etc/passwd"))
    print()
    print("Using ’secure_archive’ to read from a regular file:")
    print(f"{tup}\n")
    print("Using ’secure_archive’ to write previous content to a new file:")
    print(secure_archive("result.txt", "w", tup[1]))
