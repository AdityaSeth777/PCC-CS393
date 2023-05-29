# Counting Upper and Lower Case Characters in a String

This Python program counts the number of upper and lower case characters in a given string.

## How it Works

1. The program defines a function `string_test(s)` that takes a string `s` as input.
2. Inside the function, it initializes a dictionary `d` with two keys: `"up_CASE"` and `"low_CASE"`, both with initial values of 0.
3. The function iterates over each character `c` in the given string.
4. If the character `c` is an uppercase letter, it increments the value associated with the `"up_CASE"` key in the dictionary.
5. If the character `c` is a lowercase letter, it increments the value associated with the `"low_CASE"` key in the dictionary.
6. If the character `c` is neither an uppercase nor a lowercase letter, it does nothing.
7. After iterating through all the characters, the function prints the entered string and the counts of uppercase and lowercase characters.
8. The program prompts the user to enter a string and stores it in the variable `a`.
9. It calls the `string_test()` function with `a` as the argument.

## Example Usage

Enter the string: Hello World!
Entered String -> Hello World!
No. of upper case characters -> 2
No. of lower case characters -> 8

## Caption

"Counting the number of upper and lower case characters in a string"

This program allows users to input a string and counts the occurrences of uppercase and lowercase characters in the string. It demonstrates the use of a dictionary to keep track of the counts and the iteration over the characters in the string. The program is useful for tasks such as analyzing the distribution of upper and lower case characters in text data or checking the case sensitivity of user inputs.
