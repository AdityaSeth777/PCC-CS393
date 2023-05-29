# Creating a List of Tuples with Number and Cube

This Python program allows the user to enter a list of numbers. It then creates a new list of tuples, where each tuple consists of a number and its cube.

## How it Works

1. The program initializes an empty list `L` to store the input tuple.
2. It prompts the user to enter the elements of the tuple, separated by commas. The `split()` method is used to split the input string into individual elements, which are then converted to integers using the `int()` function. The resulting integers are added to the list `L`.
3. The program prints the original tuple entered by the user.
4. It initializes an empty list `L2` to store the tuples of number and cube.
5. Using a loop that iterates over the indices of the tuple, the program creates a tuple for each element, consisting of the number itself and its cube (calculated using the exponentiation operator `**`).
6. Each tuple is appended to the list `L2`.
7. Finally, the program prints the new list `L2`, which contains tuples of numbers and their cubes.

## Example Usage

Enter the tuple: 2, 3, 4, 5
The tuple is: (2, 3, 4, 5)
The list of number and their cubes is: [(2, 8), (3, 27), (4, 64), (5, 125)]

## Caption

"Creating a List of Tuples with Number and Cube"

This program demonstrates how to generate a list of tuples, where each tuple contains a number from the given list and its corresponding cube. It showcases the concept of list comprehension and the ability to perform calculations within tuple elements. The program is useful when there is a need to associate each number in a list with its cube, such as in mathematical or scientific computations involving cubes.
