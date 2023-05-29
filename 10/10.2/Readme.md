# Extracting Fifth Letters from Words

This Python code takes a list of words and extracts the fifth letter from each word, storing them in a new list called `fifth`. If a word is not long enough to have a fifth letter, it skips that word.

## How it Works

1. The program prompts the user to enter a list of words.
2. The input is split into individual words and stored in a list called `l`.
3. The original list of words is printed.
4. A new empty list called `fifth` is created.
5. A loop iterates over each word in the `l` list.
6. Inside the loop, a try-except block is used to handle the possibility of a word not being long enough to have a fifth letter.
7. If a word has at least five letters, the fifth letter is appended to the `fifth` list.
8. If a word is not long enough, the `IndexError` is caught by the except block and the loop continues to the next word.
9. After processing all the words, the `fifth` list containing the fifth letters (if available) is printed.

## Example Usage

Enter the words: chocolate chicken corn sandwich soup potatoes beef lox lemonade
The list of food is: ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
The list carrying fifth letters of each word is: ['l', 'k', 'w', 'w', 'p', 't']

## Caption

"A Python code to extract the fifth letter from each word in a list, handling cases where words are not long enough."

This code takes a list of words, extracts the fifth letter from each word, and stores them in a new list. It handles cases where words are not long enough by using a try-except clause to skip those words.
