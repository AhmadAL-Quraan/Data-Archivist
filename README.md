# File Operations in Python

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
