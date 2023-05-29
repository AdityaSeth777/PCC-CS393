# Pascal's Triangle

This Python program generates Pascal's Triangle based on the number of rows specified by the user.

## How it Works

1. The program imports the `factorial` function from the `math` module.
2. It prompts the user to enter the number of rows they want to print for Pascal's Triangle and stores it in the variable `n`.
3. The program uses nested loops to iterate over each row and column in the triangle.
4. In the outer loop, it iterates `i` from 0 to `n-1`, representing the row number.
5. In the inner loop, it iterates `j` from 0 to `n-i`, representing the column number and creating left spacing.
6. Inside the inner loop, it prints the binomial coefficient using the formula `nCr = n! / ((n-r)! * r!)`, where `n` is the row number and `r` is the column number.
7. The binomial coefficient is calculated by dividing the factorial of the row number (`factorial(i)`) by the product of the factorials of the column number and the difference between the row and column numbers (`factorial(j) * factorial(i-j)`).
8. After printing the coefficients for each row, the program moves to a new line for the next row.
9. The process continues until all rows are printed.

## Example Usage

Enter the number of rows you want to print for Pascal's Triangle -> 5
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1

## Caption

"Generating Pascal's Triangle based on the number of rows specified by the user"

This program allows users to input the number of rows they want to print for Pascal's Triangle. It utilizes the binomial coefficient formula and the `factorial` function to calculate the coefficients. The resulting triangle is displayed with appropriate spacing for a clear representation. Pascal's Triangle is a mathematical concept that showcases the coefficients of binomial expansions and has various applications in combinatorics and probability theory.
