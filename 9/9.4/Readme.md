# Cylinder Calculator

This Python program allows the user to enter the height and radius of a cylinder and calculates its volume and surface area using the math module.

## How it Works

1. The program defines a function named `main()`.
2. Within the `main()` function, the user is prompted to enter the height and radius of the cylinder.
3. The program uses the provided values to calculate the volume and surface area of the cylinder using the mathematical formulas:
   - Volume: `volume = π * radius^2 * height`
   - Surface Area: `surface_area = 2π * radius * height + 2π * radius^2`
4. The calculated volume and surface area are printed to the console.
5. The program checks if the `__name__` variable is equal to `'__main__'`, indicating that the program is being run directly (not imported as a module).
6. If the condition is true, the `main()` function is called.
7. This ensures that the code inside the `main()` function is only executed when the script is run directly.

## Example Usage

Height: 5
Radius: 2
Volume is: 62.83185307179586
Surface Area is: 94.24777960769379

## Caption

"A cylinder calculator to compute its volume and surface area"

This program prompts the user to enter the height and radius of a cylinder and calculates its volume and surface area using the mathematical formulas. It demonstrates basic usage of user input and the math module in Python.
