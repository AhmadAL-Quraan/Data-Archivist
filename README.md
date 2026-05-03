# File operations in python 
* `open`: Allows you to open a file in python, it will return **file-like object** .

```python 
file = open("file-name","mode")
```
`Text mode (default, e.g., 'r':read only , 'w': delete what exist and write , 'a': appened at the end of file, 'r+': If you want reading and writing -> begging of the file, a+: Read and appened at the end(need file.seek(0) to print  ): Returns a _io.TextIOWrapper object.`

`Buffered Binary mode (e.g., 'rb', 'wb', 'ab'): Returns a buffered stream object such as _io.BufferedReader, _io.BufferedWriter, or _io.BufferedRandom.`

`Raw Binary mode (e.g., 'rb' with buffering set to 0): Returns a raw stream object such as _io.FileIO. `

-> If you didn't specify, the default will be `r`.

Modes:
  
* `r`: Read from the file. 
* `w`: Write on the file .
* `a`: Append at the end of the file.
* `r+`: Read and write on the file, the pointer is at the start of the file, it will overwrite the text from the beginning.
* `a+`: Read + append, it points at the end of the file, use `file.seek(0)` to move the index to the start again then print using `file.read()`.



Methods include: standard methods like .read(), .readline(), .readlines(), .write(), and .close().

* `file.close()`: Used to 1) Flushing data to disk, 2) Releasing system resources-> Unlocks Files like on windows, prevent resource leaks and free memory.

Typing for files in python:
* `typing.IO`
```python 
import typing 
file:typing.IO = open("file","mode")
```

* `typing.TextIO` for text based streams opened with `r`.
* `typing BinaryIO`: for byte-based streams opened with `rb`.


# Common errors in files 

* Opening a file for read-only and write to it. 
```python 
file = open("file.txt","r")
file.write("hello") # This will give an error: not writeable
```



#  sys package 

## input() vs sys.stdin
  * `input()`: Slower than `sys.stdin`, read `\n` each time (you must use `strip()` or `rstrip()`.

  * Use `.readline()`, `.read()` with `sys.stdin`.

## sys.stderr

* To redirect the output to stderr -> `print("output",file=sys.stderr)`
