# Writing List Elements to a File

This Python program allows the user to enter a list of elements and a filename. It then writes each element of the list to the file, with each element on a new line.

## How it Works

1. An empty list `list1` is created to store the elements.
2. The user is prompted to enter the number of elements they want to add to the list.
3. Using a `for` loop, the program iterates `n` times to get `n` elements from the user and adds them to the `list1`.
4. The user is prompted to enter the name of the file they want to open.
5. The file is opened in write mode (`'w+'`) using a `with` statement, which ensures that the file is properly closed after writing.
6. Another `for` loop is used to iterate over each element in `list1`.
7. Within the loop, each element is written to the file using the `write` method, with the format `%s\n` to append a newline character after each element.
8. After writing all the elements, the program prints "File written successfully."
9. The file is automatically closed when the `with` block is exited.

## Example Usage

Enter number of elements: 5
Enter the element: Element 1
Enter the element: Element 2
Enter the element: Element 3
Enter the element: Element 4
Enter the element: Element 5
Enter the name of the file you want to open: myfile.txt

File written successfully.

## Caption

"Writing list elements to a file"

This program enables users to enter a list of elements and specify a filename. It then writes each element of the list to the file, with each element on a new line. This allows users to easily save and store a collection of data or information in a text file.
