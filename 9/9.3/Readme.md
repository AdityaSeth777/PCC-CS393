# Degree to Radian Converter

This Python program allows the user to enter a degree value and converts it to radians using the math module.

## How it Works

1. The program defines a function named `main()`.
2. Within the `main()` function, the user is prompted to enter a degree value.
3. The input degree value is then converted to radians by multiplying it with `math.pi / 180`.
4. The radian value is printed to the console.
5. The program checks if the `__name__` variable is equal to `'__main__'`, indicating that the program is being run directly (not imported as a module).
6. If the condition is true, the `main()` function is called.
7. This ensures that the code inside the `main()` function is only executed when the script is run directly.

## Example Usage

Degree: 45
0.7853981633974483

## Caption

"A simple degree to radian converter"

This program prompts the user to enter a degree value and converts it to radians using the mathematical formula `radian = degree * (π/180)`. It demonstrates basic usage of user input and the math module in Python.
