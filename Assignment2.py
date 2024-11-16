"""
    Author: Shaheer Mallick
    Revision Date: 8 November 2024
    Program: School Yearbook Assignment
    Description: A program to sort an amount of photos in the
    best possible dimensions to minimize perimeter and area
    Variable Dictionary: 
    get_valid_input →  is a function that asks for user input for either
    a positive integer or ‘done’
    user_input → stores input from user for number of photos or ‘done’
    number_of_photos → converts and stores the input as integer if possible
    best_perimeter → stores smallest perimeter found
    best_dimensions → stores best dimensions in rows x columns (results in min perimeter)
"""
import math  
# imports math functions 

def get_valid_input():
    user_input = input("\nInput a number of photos or type 'done' to finish: ")  
# user input for dimensions
    if user_input.lower() == "done":  
# checks if user wants to exit
        print("\nOkay!")  
# message to user after they exit
        return print("")
    try:
        number_of_photos = int(user_input)  
# input to integer
        if number_of_photos >= 1:  
# ensures input is a positive integer
            return number_of_photos  
# returns valid number of photos
        else:
            print("Please enter a positive integer.")  
# tells user to input positive integer 
            return get_valid_input()  
# calls function again to get valid input
    except ValueError:
        print("\nInvalid input. Please enter a positive integer or 'done' to exit.")  
# deals with non-integer input
        return get_valid_input()  
# calls the function repeatedly to get valid input

def find_best_dimensions(total_photos):
    best_perimeter = None
# assigns best_perimiter to nothing
    best_dimensions = (1, total_photos)  
# base dimension
    for rows in range(1, int(math.sqrt(total_photos)) + 1):  
# iterate through possible row values (sqrt function makes it efficient)
        if total_photos % rows == 0:  
# check if rows divide total_photos evenly using remainder 
            columns = total_photos // rows  
# calculates columns
            perimeter = (2 * rows) + (2 * columns) 
# calculates perimeter
            if best_perimeter is None or perimeter < best_perimeter:  
# check if this is the best perimeter
                best_perimeter = perimeter  
# update best perimeter
                best_dimensions = (rows, columns)  
# update best dimensions
    return best_dimensions, best_perimeter  
# return the best dimensions and perimeter
results = []  
# list to store results
print("Welcome to the school yearbook program!")  
# welcome message

for _ in range(100):  
# allows multiple inputs
    number_of_photos = get_valid_input()  
# gets user input
    if number_of_photos is None:  
# exit if user inputs 'done'
        break
# exit loop

    best_dimensions, best_perimeter = find_best_dimensions(number_of_photos)  
# find best dimensions and perimeter
    rows, columns = best_dimensions  
# get best dimensions
    results.append((number_of_photos, best_dimensions, best_perimeter))
# append result to list
    
    print(f"\nThe best layout for {number_of_photos} photos is {rows} x {columns} "
          f"with a perimeter of {best_perimeter}." 
          f"\n{results}")  
# output best layout

print("Photos|Dimensions|Perimeter ")  
# tells user the array format
for result in results: 
# iterate through results
    print(result)  
# print each result





