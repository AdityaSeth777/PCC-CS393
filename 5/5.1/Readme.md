# Swapping Two Tuples in Python

This Python program allows the user to enter two tuples and swaps their positions.

## How it Works

1. The program initializes an empty list `L` to store the tuples.
2. It prompts the user to enter the elements of the first tuple, separated by commas. The `split()` method is used to split the input string into individual elements, which are then converted into a tuple using the `tuple()` function. The resulting tuple is appended to the list.
3. Similarly, the program prompts the user to enter the elements of the second tuple and appends it to the list.
4. The program then prints the original first and second tuples.
5. Using tuple unpacking, the program swaps the positions of the tuples in the list by assigning the first tuple to the second tuple and vice versa.
6. Finally, the program prints the updated first and second tuples after the swap.

## Example Usage

Enter the first tuple: 1, 2, 3
Enter the second tuple: 4, 5, 6
The first tuple is: (1, 2, 3)
The second tuple is: (4, 5, 6)
After swapping, the first tuple is: (4, 5, 6)
After swapping, the second tuple is: (1, 2, 3)

## Caption

"Swapping Two Tuples in Python"

This program allows the user to enter two tuples and swaps their positions. It demonstrates the use of list manipulation, tuple creation, and tuple unpacking in Python. The program is useful when there is a need to exchange the contents of two tuples, such as when reordering or rearranging data in a specific order.
