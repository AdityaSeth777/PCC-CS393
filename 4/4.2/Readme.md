# Reversing a List in Python

This Python program allows the user to create a list of numbers, and then reverses the elements in the list.

## How it Works

1. The program initializes an empty list `lst` to store the elements.
2. It prompts the user to enter the number of elements (`n`) they want to add to the list.
3. Using a loop, the program iterates `n` times and prompts the user to enter each element, which is then appended to the list using the `append()` method.
4. After all the elements are added, the program prints the original list.
5. It initializes an empty list `l` to store the reversed elements.
6. The program iterates over each element in the original list `lst` using a loop.
7. Inside the loop, it inserts each element at the beginning of the new list `l` using the `insert()` method with an index of 0.
8. Finally, the program prints the reversed list `l`.

## Example Usage

Enter number of elements: 5
Enter the element:
10
Enter the element:
20
Enter the element:
30
Enter the element:
40
Enter the element:
50
Original List: [10, 20, 30, 40, 50]
Reversed List: [50, 40, 30, 20, 10]

## Caption

"Reversing a List in Python"

This program allows the user to create a list of numbers and reverses the order of elements in the list. It demonstrates the use of list creation, element appending, and list manipulation in Python. The program can be used to reverse any list of elements, such as numbers, strings, or other objects, and can be applied in various programming scenarios.
