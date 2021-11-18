Lab 9


Problem
Provided with this handout is a file named "movies.csv" which contains information regarding approximately 5,000 movies. Each line contains comma-separated values about each movie in the following order:

release date
title
budget
box office gross
Write a program which, given the name of a file respecting this format and the name of an output file, writes all movie information from the input file to the output file, but also adds a new column with the movie's profit (computed as the difference between box office gross and budget). Additionally, the program should determine which movies had the highest and lowest profits and output to the console all information related to those two movies.

Instructions
Create a new Python file and place intro comments using the template below.
Use comments to write the algorithm your program will follow, including functions.
Write the Python code corresponding to each of your algorithm's steps.
Commit and push changes and check your repository on github.com to confirm your updates before leaving lab (even if not finished).

Note: This lab does not require a flowchart or test cases.

Intro comments template
# Programmers: [your names]
# Course: CS151, Dr. Rajeev  
# Date:
# Lab Number:
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]
Function decomposition
Your program should have a function for each of the following tasks. Practice iterative development: implement each item according to the instructions section below and then test that your code still works before proceeding onto the next item.

A function load_movie_data which, given the name of a file respecting the csv format outlined above, loads the data into a list of lists. Declare column index constants at the top of your program for each of the movie fields (release date, title, etc.) Cast each field to the appropriate type. Use try/except so that your program exits normally if the file does not exist or if a numerical value in the input file fails to cast.
A function add_profit_column which, given a movie dataset as a list of lists, adds a profit column to the data computed as the difference between each movie's gross and its budget.
A function print_min_and_max_profit which, given a movie dataset as a list of lists, searches the dataset and prints all available info on the movies with the highest and lowest profits.
A function save_movie_data which, given a movie dataset as a list of lists and a filename, saves the dataset to a comma-separated values file of the given name.
A main function to drive the program.
Submission
One submission per team including all member names.

GitHub: Completed .py file (including intro and algorithm comments).
