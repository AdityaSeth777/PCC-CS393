# Counting Positive and Negative Numbers in a List

This Python program allows the user to create a list of numbers and counts the number of positive and negative numbers in the list.

## How it Works

1. The program initializes an empty list `lst` to store the elements.
2. It prompts the user to enter the number of elements (`n`) they want to add to the list.
3. Using a loop, the program iterates `n` times and prompts the user to enter each element, which is then appended to the list using the `append()` method.
4. After all the elements are added, the program prints the original list.
5. It initializes variables `pos_count` and `neg_count` to keep track of the counts of positive and negative numbers, respectively.
6. The program iterates through each number in the list using a loop.
7. For each number, it checks if the number is greater than or equal to zero. If so, it increments the `pos_count` variable. Otherwise, it increments the `neg_count` variable.
8. Finally, the program prints the counts of positive and negative numbers.

## Example Usage

Enter number of elements: 5
1
-2
3
-4
5
Original List: [1, -2, 3, -4, 5]
Positive numbers in the list: 3
Negative numbers in the list: 2

## Caption

"Counting Positive and Negative Numbers in a List"

This program allows the user to create a list of numbers and counts the number of positive and negative numbers in the list. It demonstrates the use of list creation, element appending, and iterative counting in Python. The program is useful for analyzing datasets that contain positive and negative numbers and provides a simple way to calculate their respective counts.
