# Counting Word Occurrences in a File

This Python program allows the user to enter a word and the name of a file. It opens the file and counts the occurrences of the specified word within the file.

## How it Works

1. The user is prompted to enter a word.
2. The user is prompted to enter the name of the file they want to open.
3. Using a `with` statement, the file is opened in read mode (`'r'`).
4. A `for` loop is used to iterate over each line in the file.
5. Within the loop, the line is split into words using the `split()` method.
6. Another `for` loop is used to iterate over each word in the line.
7. If a word matches the specified word, the count is incremented by 1.
8. After iterating over all the lines and words, the program prints the count of occurrences of the word.
9. The file is automatically closed when the `with` block is exited.

## Example Usage

Enter the word: apple
Enter the name of the file you want to open: text.txt

Occurrences of the word "apple": 3

## Caption

"Counting word occurrences in a file"

This program allows users to specify a word and a file. It opens the file, reads its content, and counts how many times the specified word appears within the file. This can be useful for analyzing the frequency of specific words within a text document.
