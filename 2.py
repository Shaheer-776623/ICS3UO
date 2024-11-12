"""
    Author: Shaheer Mallick
    Revision Date: 8 November 2024
    Program: School Yearbook Assignment
    Description: A program to sort an amount of photos in the
    best possible format to savespace
    Variable Dictionary:
"""


def get_valid_input():
        user_input = input("Input a number of photos (or type 'done' to finish): ")
        if user_input == "done":
            print("Okay!")
            

try:
    # Convert input to an integer and validate
    number_of_photos = int(user_input)
    if number_of_photos >= 1:
        return number_of_photos
 else:
     print("%d is not a valid number",number_of_photos,
        "Please enter a positive number.")
except ValueError:
            print("The number is not a positive integer.")
                
