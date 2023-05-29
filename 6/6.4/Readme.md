# String Replacement

This Python program demonstrates string replacement using a dictionary.

## How it Works

1. The program prompts the user to enter a string (`test_str`).
2. The program prompts the user to enter the number of elements in the replacement dictionary (`repl_dict`).
3. Using a loop that iterates `n` times, the program collects key-value pairs for the replacement dictionary.
4. The program iterates over each key in the replacement dictionary.
   - It replaces all occurrences of the key in the `test_str` with its corresponding value using the `replace()` function.
5. The program prints the modified string, `test_str`.

## Example Usage

Enter the string: Hello {name}, how are you?
Enter the number of elements in the dictionary: 1
Enter the key: {name}
Enter the value: John
The string is: Hello John, how are you?

## Caption

"String Replacement using Dictionary"

This program allows users to replace specific substrings in a string using a dictionary. It provides a convenient way to perform multiple replacements in a single step. The program is useful for text manipulation tasks that involve substituting placeholders or tokens with corresponding values.
