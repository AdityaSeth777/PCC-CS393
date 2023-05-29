# Read File Head

This Python program reads the specified number of lines from the beginning of a file.

## How it Works

1. The program defines a function called `file_read_from_head` that takes two parameters: `fname` (the name of the file to be read) and `nlines` (the number of lines to be read from the file).
2. Inside the function, the `islice` function from the `itertools` module is used to read the specified number of lines from the file.
3. The `open` function is used to open the file in a context manager, ensuring that the file is automatically closed after reading.
4. Using a `for` loop, the program iterates over the lines returned by `islice` and prints each line.
5. In the main part of the program, the user is prompted to enter the number of lines they want to read and the name of the file they want to open.
6. The program calls the `file_read_from_head` function with the user-provided values of `fname` and `nlines` to read and display the specified number of lines from the file.

## Example Usage

Enter the number of lines to be read: 5
Enter the name of the file you want to open: myfile.txt

Contents of the file (first 5 lines):
Line 1
Line 2
Line 3
Line 4
Line 5

## Caption

"Reading the specified number of lines from the beginning of a file"

This program allows users to input the number of lines they want to read from a file and the name of the file they want to open. It uses the `file_read_from_head` function to read the specified number of lines from the file and prints them to the console. This provides a convenient way to quickly view the beginning of a file without reading the entire file.
