# Copying File Content

This Python program allows the user to enter two filenames. It then reads the content from the first file and appends it to the second file.

## How it Works

1. The user is prompted to enter the names of two files they want to open.
2. Using a `with` statement, both files are opened simultaneously. The first file is opened in read mode (`'r'`), while the second file is opened in append mode (`'a'`).
3. A `for` loop is used to iterate over each line in the first file.
4. Within the loop, each line is written to the second file using the `write` method, effectively appending the content.
5. After copying all the content, the program prints "Copied successfully."
6. The files are automatically closed when the `with` block is exited.

## Example Usage

Enter the name of the first file you want to open: input.txt
Enter the name of the second file you want to open: output.txt

Copied successfully.

## Caption

"Copying file content"

This program enables users to specify two files: a source file and a destination file. It reads the content from the source file and appends it to the destination file. This provides an easy way to duplicate or merge the content of files.
