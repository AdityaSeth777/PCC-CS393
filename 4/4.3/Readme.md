# Counting Even and Odd Numbers in a List

This Python program allows the user to create a list of numbers and counts the number of even and odd elements in the list.

## How it Works

1. The program initializes an empty list `lst` to store the elements.
2. It prompts the user to enter the number of elements (`n`) they want to add to the list.
3. Using a loop, the program iterates `n` times and prompts the user to enter each element, which is then appended to the list using the `append()` method.
4. After all the elements are added, the program prints the original list.
5. It initializes variables `even_count` and `odd_count` to keep track of the counts of even and odd numbers, respectively.
6. The program uses a while loop to iterate over each element in the list.
7. Inside the loop, it checks if the current element is divisible by 2 (even) or not.
8. If the element is even, it increments the `even_count` variable by 1; otherwise, it increments the `odd_count` variable by 1.
9. Finally, the program prints the counts of even and odd numbers in the list.

## Example Usage

Enter number of elements: 6
10
15
20
25
30
35
Original List: [10, 15, 20, 25, 30, 35]
Even numbers in the list: 3
Odd numbers in the list: 3

## Caption

"Counting Even and Odd Numbers in a List"

This program allows the user to create a list of numbers and counts the number of even and odd elements in the list. It demonstrates the use of list creation, element appending, and iteration with a while loop in Python. The program is useful for analyzing numerical data and determining the distribution of even and odd numbers in a given list.
