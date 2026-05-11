# File Operations in Python

* Understanding how to deal with files in python, including reading, writing, parsing and handle different errors.
* Main concepts on that explained below, also what I learnt from each [exercise](#python-file-handling--sys-module-exercises-ex00--ex03))
## Opening Files with `open()`

The `open()` function opens a file and returns a **file object** (also called a *file-like object*).

```python
file = open("file_name", "mode")
```

If no mode is specified, Python uses `"r"` (read mode) by default.

---

# File Modes

| Mode | Description |
|---|---|
| `"r"` | Read-only mode (default). Raises an error if the file does not exist. |
| `"w"` | Write mode. Creates a new file or overwrites existing content. |
| `"a"` | Append mode. Writes data at the end of the file. |
| `"r+"` | Read and write mode. Starts at the beginning of the file. Writing overwrites existing content. |
| `"a+"` | Read and append mode. File pointer starts at the end of the file. Use `seek(0)` to read from the beginning. |
| `"rb"` | Read binary mode. |
| `"wb"` | Write binary mode. |
| `"ab"` | Append binary mode. |

---

# Types of File Objects

## 1. Text Mode (Default)

Examples:

```python
open("file.txt", "r")
open("file.txt", "w")
```

Returns:

```python
_io.TextIOWrapper
```

---

## 2. Buffered Binary Mode

Examples:

```python
open("file.bin", "rb")
open("file.bin", "wb")
```

Returns buffered binary stream objects such as:

- `_io.BufferedReader`
- `_io.BufferedWriter`
- `_io.BufferedRandom`

---

## 3. Raw Binary Mode

Example:

```python
open("file.bin", "rb", buffering=0)
```

Returns:

```python
_io.FileIO
```

---

# Common File Methods

| Method | Description |
|---|---|
| `read()` | Reads the entire file (or a specific number of characters). |
| `readline()` | Reads one line at a time. |
| `readlines()` | Reads all lines and returns them as a list. |
| `write()` | Writes text to the file. |
| `close()` | Closes the file and releases resources. |
| `seek(pos)` | Moves the file pointer to a specific position. |
| `tell()` | Returns the current file pointer position. |

---

# Example: Reading a File

```python
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# Example: Writing to a File

```python
file = open("data.txt", "w")

file.write("Hello World")

file.close()
```

---

# Example: Appending to a File

```python
file = open("data.txt", "a")

file.write("\nNew line")

file.close()
```

---

# Example: `r+` Mode

```python
file = open("data.txt", "r+")

print(file.read())

file.write("NEW")

file.close()
```

> Writing starts from the current pointer position and may overwrite existing text.

---

# Example: `a+` Mode

```python
file = open("data.txt", "a+")

file.write("\nAppended text")

file.seek(0)

print(file.read())

file.close()
```

> `a+` starts at the end of the file, so you usually need `seek(0)` before reading.

---

# Why `close()` is Important

```python
file.close()
```

Closing a file:

1. Flushes buffered data to disk.
2. Releases system resources.
3. Prevents memory/resource leaks.
4. Unlocks the file on some operating systems (like Windows).

---

# Better Way: Using `with`

Using `with` automatically closes the file.

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

This is the preferred and safer approach.

---

# Typing Files in Python

```python
import typing

file: typing.IO = open("data.txt", "r")
```

## Text Files

```python
import typing

file: typing.TextIO = open("data.txt", "r")
```

## Binary Files

```python
import typing

file: typing.BinaryIO = open("image.png", "rb")
```

---

# Common File Errors

## Writing to a Read-Only File

```python
file = open("data.txt", "r")

file.write("Hello")
```

Error:

```python
io.UnsupportedOperation: not writable
```

---

## Opening a Missing File

```python
file = open("missing.txt", "r")
```

Error:

```python
FileNotFoundError
```

---

# The `sys` Module

```python
import sys
```

---

# `input()` vs `sys.stdin`

## `input()`

```python
name = input()
```

- Easy to use.
- Slower for large input.
- Removes the newline automatically.

---

## `sys.stdin.readline()`

```python
import sys

line = sys.stdin.readline()
```

- Faster than `input()`.
- Keeps the newline character `\n`.
- Usually used in competitive programming.

Example:

```python
line = sys.stdin.readline().strip()
```

---

# Reading Entire Input

```python
import sys

data = sys.stdin.read()
```

Useful when reading large input at once.

---

# Writing to `stderr`

```python
import sys

print("Error message", file=sys.stderr)
```

`stderr` is commonly used for:

- Debugging
- Logging errors
- Separating errors from normal output

---

# Quick Summary

| Task | Mode / Method |
|---|---|
| Read file | `"r"` |
| Write and overwrite | `"w"` |
| Append | `"a"` |
| Read + write | `"r+"` |
| Read + append | `"a+"` |
| Binary reading | `"rb"` |
| Move pointer | `seek()` |
| Current position | `tell()` |
| Auto-close files | `with open(...)` |
| Fast input | `sys.stdin.readline()` |
| Error output | `sys.stderr` |

---



# Python File Handling & `sys` Module Exercises (ex00 → ex03)

* Disscusing what I learnt and should be learned from each exercise.
---

# ex00 — Basic File Reading

## Concepts Introduced

### 1. Command Line Arguments

Using `sys.argv` to access arguments passed to the program.

```python
import sys

print(sys.argv)
```

Example:

```bash
python3 script.py file.txt
```

- `sys.argv[0]` → script name
- `sys.argv[1]` → first argument

---

### 2. Argument Validation

```python
if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
    exit(0)
```

Learned:

- Checking user input before running the program
- Preventing invalid usage

---

### 3. Opening Files

```python
file_open = open(sys.argv[1], "r")
```

Learned:

- Using `open()`
- Read mode `"r"`

---

### 4. Reading File Content

```python
print(file_open.read())
```

Learned:

- `.read()` reads the entire file as one string

---

### 5. Closing Files

```python
file_open.close()
```

Learned:

- Releasing resources
- Proper file cleanup

---

### 6. Exception Handling

```python
except Exception as e:
    print(f"Error opening file '{sys.argv[1]}': {e}")
```

Learned:

- Preventing program crashes
- Handling runtime errors safely

---

# What Should Be Learned from ex00

- How to use `sys.argv`
- Basic file opening and reading
- Importance of closing files
- Basic exception handling
- Simple CLI program structure

---

# ex01 — File Transformation & Writing

This exercise extends ex00 by transforming and saving data.

---

## New Concepts Introduced

### 1. Storing File Content

```python
content: str = file_open.read()
```

Learned:

- Saving file data into variables

---




### 2. Writing to Files

```python
new_file = open(inp, "w")
new_file.write(List_after)
```

Learned:

- Write mode `"w"`
- Creating new files
- Saving processed data

---

# What Should Be Learned from ex01

- Reading and modifying text
- Creating transformed output
- Writing data to files
- Interactive terminal programs
- Basic text-processing algorithms

---

# ex02 — `sys.stdin`, `stdout`, and `stderr`

This exercise improves terminal interaction using the `sys` module.

---

## New Concepts Introduced

### 1. Using `sys.stdin.readline()`

```python
inp = sys.stdin.readline().rstrip().strip()
```

Learned:

- Faster input handling
- Difference between `input()` and `sys.stdin.readline()`
- Removing `\n` using `.rstrip()` or `.strip()`

---

### 2. Using `sys.stdout.write()`

```python
sys.stdout.write("Not saving data")
```

Learned:

- Direct writing to standard output
- Difference between `print()` and `stdout.write()`

---

### 3. Using `sys.stderr`

```python
print(
    f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
    file=sys.stderr,
)
```

Learned:

- Writing errors separately from normal output
- Debugging and logging concepts

---

# What Should Be Learned from ex02

- Standard input/output streams
- Faster terminal input methods
- Error stream handling
- Better CLI application design

---

# ex03 — Secure File Handling with Functions

This exercise introduces reusable file-handling functions and safer file management.

---

## New Concepts Introduced

### 1. Creating Reusable Functions

```python
def secure_archive(file_name: str, mode: str = "r", content: str = ""):
```

Learned:

- Function design
- Reusability
- Default arguments

---


### 2. Using `with open()`

```python
with open(file_name, mode) as file:
```

Learned:

- Automatic file closing
- Safer resource management
- Preferred Python file handling style

---

### 3. Returning Status Information

```python
return (True, full_content)
```

Learned:

- Returning multiple values
- Error-state design patterns

---

### 4. Supporting Multiple Modes

```python
if mode == "r":
elif mode == "w":
```

Learned:

- Multi-purpose functions
- Conditional logic in APIs

---

### 5. Handling File Errors Gracefully

```python
except Exception as e:
    return (False, f"{e}")
```

Learned:

---
- Safe error propagation
- Designing fault-tolerant code

---

# What Should Be Learned from ex03

- Writing reusable utility functions
- Safe file handling using `with`
- Returning structured results
- Better error management
- Designing cleaner APIs

---

# Overall Topics Covered (ex00 → ex03)

## File Handling

- `open()`
- `read()`
- `write()`
- `close()`
- `with open()`

---

## File Modes

| Mode | Purpose |
|---|---|
| `"r"` | Read |
| `"w"` | Write |
| `"a"` | Append |
| `"r+"` | Read + Write |
| `"a+"` | Read + Append |

---

## `sys` Module

- `sys.argv`
- `sys.stdin`
- `sys.stdout`
- `sys.stderr`

---

## Error Handling

- `try`
- `except`
- Preventing crashes

---


## Good Practices Learned

### Preferred File Handling

```python
with open("file.txt", "r") as file:
    content = file.read()
```

Instead of:

```python
file = open("file.txt", "r")
content = file.read()
file.close()
```

---


### Separating Errors from Output

```python
print("error", file=sys.stderr)
```


