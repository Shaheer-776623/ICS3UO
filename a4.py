"""
Author: Shaheer Mallick
Revision Date: 20 December 2024
Program: Reading and Searching for past Wordle Data
Description: A program to take an input from the user for a
date or a word and output when it was the Wordle and what the
word was.
months: mapping month abbreviations to two-digit numbers
words_dates: Dictionary to store words and their corresponding dates,
month_number: Two-digit string representation of the month
day_number: Two-digit string representation of the day
search_word: Word input by the user to search in the database
search_date: Date input by the user to search for a word in the database
result_date: Date corresponding to the searched word
found_word: Word corresponding to the searched date
"""
# Converts month abbreviation to a two-digit number
def month_to_number(month):
    months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05",
              "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10",
              "Nov": "11", "Dec": "12"}  # Dictionary of months
    return months.get(month, "00")  # Return corresponding number or "00" if invalid

# Merges day, month, and year into a single integer
def merge(day, month, year):
    if len(day) == 1:  # Manually add zero if single digit
        day = '0' + day
    month_number = month_to_number(month)  # Convert month
    return int(year + month_number + day)  # Combine into number

# Recursively checks if a word exists and returns corresponding date
def isMatch(word, words, dates, index=0):
    if index >= len(words):  # Base case: end of list
        return 0  # No match found
    if words[index].lower() == word.lower():  # Match found
        return dates[index]  # Return corresponding date
    return isMatch(word, words, dates, index + 1)  # Recurse through list

# Reads file and stores data
try:
    file = open("wordle.dat", "r")  # Open file
    lines = file.readlines()  # Read lines
    file.close()  # Close file

    dates, words = [], []  # Creates arrays

    # Processes each line in the file
    for line in lines:
        month, day, year, word = line.split()  # Split line
        dates.append(merge(day, month, year))  # Add date to list
        words.append(word)  # Add word to list
except FileNotFoundError:
    print("Error: The file 'wordle.dat' was not found. Please check the file and try again.")
    input("Press Enter to exit.")  # Prevent immediate exit
    exit()

# Main logic: interact with user
print("Welcome to the Wordle Database!")  # Print welcome message

# Function to get valid choice input
def get_choice():
    choice = input("Enter 'w' if you are looking for a word, or 'd' for a word on a certain date: ").strip().lower()  # Get user choice
    if choice not in ['w', 'd']:  # Validate input
        print("Invalid input. Please enter 'w' or 'd'.")  # Print error message
        return get_choice()  # Retry
    return choice  # Return valid choice

choice = get_choice()  # Get valid choice

if choice == 'w':  # If searching for a word
    search_word = input("What word are you looking for? ").strip()  # Get word to search
    result_date = isMatch(search_word, words, dates)  # Find matching date
    if result_date:  # If match found
        print(f"The word {search_word.upper()} was the solution to the puzzle on {result_date}.")  # Print result
    else:  # No match found
        print(f"The word '{search_word.upper()}' was not found in the database.")  # Print message
elif choice == 'd':  # If searching by date
    def get_date_input():
        try:
            year = input("Enter the year: ").strip()  # Get year
            month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ").strip().capitalize()  # Get month
            day = input("Enter the day: ").strip()  # Get day
            if len(day) == 1:  # Manually add zero if single digit
                day = '0' + day
            return merge(day, month, year)  # Merge date components
        except (ValueError, KeyError):  # Handle invalid input
            print("Invalid date format. Please try again.")  # Print error message
            return get_date_input()  # Retry
    search_date = get_date_input()  # Get valid date

    if search_date < 20210619:  # Date too early
        print(f"{search_date} is too early. No wordles occurred before 20210619. Enter a later date.")  # Print message
    elif search_date > 20240421:  # Date too recent
        print(f"{search_date} is too recent. Our records only go as late as 20240421. Please enter an earlier date.")  # Print message
    else:  # Valid date
        found_word = None  # Initialize found word
        for i in range(len(dates)):  # Iterates through dates
            if dates[i] == search_date:  # Check for match
                found_word = words[i]  # Assign matching word
                break  # Exit loop
        if found_word:  # If match found
            print(f"The word entered on {search_date} was {found_word}.")  # Print result
        else:  # No match found
            print(f"No word found for the date {search_date}.")  # Print message
else:  # Invalid input
    print("Invalid input. Please enter 'w' or 'd'.")  # Print message
