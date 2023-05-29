# Modulo of Tuple Elements in Python

This Python program allows the user to enter two tuples of equal length. It then performs the following operation:

- Calculates the modulo of corresponding elements in the tuples and stores the results in a new tuple.

## How it Works

1. The program initializes an empty list `L` to store the tuples.
2. It prompts the user to enter the elements of the first tuple, separated by commas. The `split()` method is used to split the input string into individual elements, which are then converted into a tuple using the `tuple()` function. The resulting tuple is appended to the list `L`.
3. The program prompts the user to enter the elements of the second tuple in a similar manner. This tuple is also appended to the list `L`.
4. The program checks if the two tuples have equal lengths. If not, it prints an error message and terminates.
5. If the tuples have equal lengths, the program proceeds to print the original tuples.
6. It initializes an empty list `L3` to store the modulo results.
7. Using a loop that iterates over the indices of the tuples, the program calculates the modulo of corresponding elements in the first and second tuples and appends the results to `L3`.
8. The program prints the new tuple `L3`, which contains the modulo of tuple elements.

## Example Usage

Enter the first tuple: 4, 9, 7
Enter the second tuple: 2, 3, 5
The first tuple is: (4, 9, 7)
The second tuple is: (2, 3, 5)
The new tuple is: (0, 0, 2)

## Caption

"Modulo of Tuple Elements in Python"

This program demonstrates how to calculate the modulo of corresponding elements in two tuples and store the results in a new tuple. It showcases the versatility of tuples in Python and their ability to perform element-wise operations. The program is useful when there is a need to perform mathematical computations on tuple elements, such as finding remainders or calculating modular arithmetic.
