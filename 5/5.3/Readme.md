# Adding Tuple to List and Vice Versa in Python

This Python program allows the user to enter a tuple and a list. It then performs the following operations:

- Adds the tuple elements to the list
- Concatenates the list elements to the tuple

## How it Works

1. The program initializes an empty list `L` to store the tuple.
2. It prompts the user to enter the elements of the tuple, separated by commas. The `split()` method is used to split the input string into individual elements, which are then converted into a tuple using the `tuple()` function. The resulting tuple is appended to the list `L`.
3. The program prints the original tuple.
4. It enters a loop to allow the user to enter elements for the list. The entered elements are stored in the list `L2`.
5. Inside the loop, the program prompts the user to enter an element and adds it to the list `L2`.
6. The program asks the user if they want to continue entering elements or exit the loop.
7. If the user chooses to continue (`y`), the loop continues. Otherwise, the loop breaks and the program moves to the next step.
8. The program prints the final list `L2`.
9. It creates a new list `L3` by concatenating the elements of `L2` and the tuple stored in `L`.
10. The program prints the new list `L3`.
11. It updates the tuple stored in `L` by concatenating the elements of `L2`.
12. The program prints the updated tuple stored in `L`.

## Example Usage

Enter the first tuple: 1, 2, 3
The tuple is: (1, 2, 3)
Enter the list:
Enter the element: 4
Enter 'y' to continue or end to exit: y
Enter the element: 5
Enter 'y' to continue or end to exit: end
The list is: [4, 5]
The new list is: [4, 5, 1, 2, 3]
The new tuple is: (1, 2, 3, 4, 5)

## Caption

"Adding Tuple to List and Vice Versa in Python"

This program demonstrates how to add tuple elements to a list and concatenate list elements to a tuple in Python. It showcases the flexibility of Python's data structures and their interconversion. The program is useful when there is a need to combine tuples and lists, enabling operations across different data structures.
