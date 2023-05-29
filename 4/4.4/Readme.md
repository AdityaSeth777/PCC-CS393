# Finding the Second Largest Element in a List

This Python program allows the user to create a list of numbers, removes duplicates, sorts the list, and then prints the second largest element.

## How it Works

1. The program initializes an empty list `lst` to store the elements.
2. It prompts the user to enter the number of elements (`n`) they want to add to the list.
3. Using a loop, the program iterates `n` times and prompts the user to enter each element, which is then appended to the list using the `append()` method.
4. After all the elements are added, the program prints the original list.
5. The program creates a new list `list2` by converting the original list `lst` to a set to remove duplicates and then converting it back to a list.
6. It sorts the `list2` in ascending order using the `sort()` method.
7. Finally, the program prints the second largest element in the list using indexing (`list2[-2]`).

## Example Usage

Enter number of elements: 6
10
15
20
10
25
30
Original List: [10, 15, 20, 10, 25, 30]
Second largest element is: 25

## Caption

"Finding the Second Largest Element in a List"

This program allows the user to create a list of numbers, removes duplicates, sorts the list, and then finds and prints the second largest element. It demonstrates the use of list creation, element appending, set conversion for duplicate removal, list sorting, and indexing in Python. The program is useful for extracting specific elements from a list based on their values, such as finding the second largest number in a dataset.
