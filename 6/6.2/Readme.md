# Student Grade Calculation

This Python program allows the user to enter details of multiple students, including their assignment marks, test marks, and lab marks. It calculates the average marks and assigns a letter grade based on the average.

## How it Works

1. The program prompts the user to enter the number of students.
2. Using a loop that iterates `n` times, the program collects the following information for each student:
   - Name of the student
   - Assignment marks (4 inputs)
   - Test marks (2 inputs)
   - Lab marks (2 inputs)
3. For each student, the program creates a dictionary `d` to store their information, with keys for name, assignment, test, and lab.
4. The program prints the dictionary containing the student's information.
5. It calculates the average marks for the student using the given weightage: 10% for assignments, 70% for tests, and 20% for labs.
6. Based on the average marks, the program assigns a letter grade to the student:
   - A: Average marks >= 90
   - B: Average marks >= 80
   - C: Average marks >= 70
   - D: Average marks < 70
7. The program prints the average marks and the letter grade for the student.
8. The loop repeats for the next student until all students' information has been processed.

## Example Usage

Enter the number of students: 2

Enter the name of the student: John
Enter the assignment marks: 90
Enter the assignment marks: 85
Enter the assignment marks: 92
Enter the assignment marks: 88
Enter the test marks: 85
Enter the test marks: 88
Enter the lab marks: 90.5
Enter the lab marks: 92.5
The dictionary is: {'name': 'John', 'assignment': [90, 85, 92, 88], 'test': [85, 88], 'lab': [90.5, 92.5]}
The average marks of John is: 88.1
The letter grade of John is: B

Enter the name of the student: Jane
Enter the assignment marks: 80
Enter the assignment marks: 75
Enter the assignment marks: 78
Enter the assignment marks: 82
Enter the test marks: 76
Enter the test marks: 80
Enter the lab marks: 84.5
Enter the lab marks: 88.5
The dictionary is: {'name': 'Jane', 'assignment': [80, 75, 78, 82], 'test': [76, 80], 'lab': [84.5, 88.5]}
The average marks of Jane is: 79.9
The letter grade of Jane is: C

## Caption

"Calculating and Assigning Grades for Students"

This program allows users to input student details such as assignment marks, test marks, and lab marks. It calculates the average marks for each student using predefined weightages and assigns letter grades based on the averages. The program is useful for educators or institutions seeking to automate the process of grading students and providing letter grades.
