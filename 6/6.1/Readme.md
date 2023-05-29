# Sorting a Dictionary by Key and Value

This Python program allows the user to enter a dictionary with key-value pairs. It then sorts the dictionary by key and value and prints the sorted dictionaries.

## How it Works

1. The program prompts the user to enter the number of elements in the dictionary.
2. It initializes an empty dictionary `d` to store the key-value pairs.
3. Using a loop that iterates `n` times, the program prompts the user to enter a key and its corresponding value. The user inputs are stored in the dictionary `d`, where each key is associated with its respective value.
4. The program prints the original dictionary entered by the user.
5. It uses the `sorted()` function to sort the dictionary `d` by key. The `sorted()` function returns a list of tuples representing the key-value pairs, which are printed as the sorted dictionary by key.
6. To sort the dictionary by value, the `sorted()` function is used again, but with an additional `key` argument. The `lambda` function `lambda x: x[1]` is used as the `key` argument to specify that the sorting should be based on the second element (value) of each tuple.
7. The sorted dictionary by value, represented as a list of tuples, is printed.

## Example Usage

Enter the number of elements in the dictionary: 3
Enter the key: apple
Enter the value: red
Enter the key: banana
Enter the value: yellow
Enter the key: cherry
Enter the value: red
The dictionary is: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
The sorted dictionary by key is: [('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red')]
The sorted dictionary by value is: [('apple', 'red'), ('cherry', 'red'), ('banana', 'yellow')]

## Caption

"Sorting a Dictionary by Key and Value"

This program demonstrates how to sort a dictionary by its keys and values. It showcases the usage of the `sorted()` function with dictionaries, providing options to sort either by key or value. The program is useful in scenarios where it is necessary to organize the elements of a dictionary in a specific order, enabling easier access and retrieval of key-value pairs.
