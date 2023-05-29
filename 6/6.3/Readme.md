# Dictionary Operations

This Python program demonstrates various operations on dictionaries, including merging dictionaries and retrieving values based on keys.

## How it Works

1. The program prompts the user to enter the number of elements in the first dictionary (`d1`).
2. Using a loop that iterates `n` times, the program collects key-value pairs for `d1`.
3. The program prints the first dictionary, `d1`.
4. The program prompts the user to enter the number of elements in the second dictionary (`d2`).
5. Using a loop that iterates `n` times, the program collects key-value pairs for `d2`.
6. The program prints the second dictionary, `d2`.
7. The program checks for each key in `d1` if it exists in `d2`.
   - If the key exists, it prints the corresponding value from `d2`.
   - If the key doesn't exist, it prints a message indicating that the key is not found in the dictionary.
8. The program merges `d1` and `d2` into a new dictionary, `d3`, by copying all key-value pairs from both dictionaries.
9. It prints the merged dictionary, `d3`.

## Example Usage

Enter the number of elements in the dictionary: 3
Enter the key: name
Enter the value: John
Enter the key: age
Enter the value: 25
Enter the key: city
Enter the value: New York
The dictionary is: {'name': 'John', 'age': '25', 'city': 'New York'}

Enter the number of elements in the dictionary: 2
Enter the key: occupation
Enter the value: Engineer
Enter the key: city
Enter the value: San Francisco
The dictionary is: {'occupation': 'Engineer', 'city': 'San Francisco'}

The value of name is: John
The value of age is: 25
The value of city is: San Francisco
The key occupation is not found in the dictionary
The merged dictionary is: {'name': 'John', 'age': '25', 'city': 'San Francisco', 'occupation': 'Engineer'}

## Caption

"Dictionary Manipulation and Merging"

This program allows users to create and manipulate dictionaries. It demonstrates operations such as retrieving values based on keys, merging dictionaries, and handling key-not-found scenarios. The program is useful for managing key-value data and performing dictionary operations efficiently.
