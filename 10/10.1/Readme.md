# Blog Post Tracker

This Python program allows the user to create a list of blog posts and track the number of photos, comments, likes, and shares for each post.

## How it Works

1. The program initializes an empty list named `blogposts`.
2. A while loop is used to continuously prompt the user for input and add new blog posts to the list.
3. Inside the loop, a dictionary named `d` is created to store the details of each blog post.
4. The user is prompted to enter the number of photos, comments, likes, and shares for the current blog post.
5. If any of these values are non-zero, they are added to the dictionary.
6. The dictionary is then appended to the `blogposts` list.
7. After adding a blog post, the user is asked if they want to add more posts. If they enter 1, the loop continues; otherwise, it breaks.
8. Once the loop ends, the original list of blog posts is printed.
9. The code calculates the total number of likes across all blog posts by iterating over each post and summing up the "likes" values. If a blog post does not have a "likes" key, it is set to zero before summing.
10. Finally, the updated list of blog posts is printed.

## Example Usage

Enter the number of photos: 3
Enter the number of comments: 10
Enter the number of likes: 25
Enter the number of shares: 5
Do you want to add more? Enter 1: 1
Enter the number of photos: 0
Enter the number of comments: 7
Enter the number of likes: 0
Enter the number of shares: 2
Do you want to add more? Enter 1: 0

The original blog post:
[{'photos': 3, 'comments': 10, 'likes': 25, 'shares': 5}, {'comments': 7, 'shares': 2}]

The total likes in the blog post: 25

The changed blog post:
[{'photos': 3, 'comments': 10, 'likes': 25, 'shares': 5}, {'comments': 7, 'likes': 0, 'shares': 2}]

## Caption

"A blog post tracker to keep count of photos, comments, likes, and shares for each post"

This program allows the user to create a list of blog posts and track the number of photos, comments, likes, and shares for each post. It provides functionality to add multiple posts, calculate the total likes, and handles missing "likes" values by setting them to zero.
