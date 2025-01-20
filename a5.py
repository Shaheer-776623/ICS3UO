"""
Author : Shaheer Mallick
Student Number: 776623
Revision date : 20 Jan 2025
Program : Credit Card Report
Description : Report of all credit cards in the customer database that have expired.
Variable Dictionary:
    file_name: str - Name of the file
    file_handle: file object - File handle
    user_names: list - List of names (first and last)
    card_numbers: list - List of credit card numbers
    card_types: list - List of credit card types
    expiration_dates: list - List of expiry dates
    data_lines: list - List of all the lines in file
    header_line: str - First line of the file (to be removed from data_lines)
    result_file: file object - File handle for the output file
    status_text: str - Text to display when expired
"""

def merge_sort(array1, array2, array3, array4, left, right):
    """
    Function to perform merge sort on four arrays.
    Parameters:
        array1 (list): Array to be sorted.
        array2, array3, array4 (list): Other arrays to be sorted.
        left (int): Left index of the subarray.
        right (int): Right index of the subarray.
    """
    if left < right:
        middle = left + (right - left) // 2

        # Recursively sorts the left half of the array
        merge_sort(array1, array2, array3, array4, left, middle)

        # Recursively sorts the right half of the array
        merge_sort(array1, array2, array3, array4, middle + 1, right)

        # Merges the two sorted halves
        merge(array1, array2, array3, array4, left, middle, right)

def merge(array1, array2, array3, array4, left, middle, right):
    """
    Function to merge two sorted arrays.
    Parameters:
        array1 (list): Array to be sorted.
        array2, array3, array4 (list): Other arrays to be sorted.
        left (int): Left index of the subarray.
        middle (int): Middle index of the subarray.
        right (int): Right index of the subarray.
    """
    n1 = middle - left + 1
    n2 = right - middle

    L1 = [array1[left + i] for i in range(n1)]
    L2 = [array2[left + i] for i in range(n1)]
    L3 = [array3[left + i] for i in range(n1)]
    L4 = [array4[left + i] for i in range(n1)]

    R1 = [array1[middle + 1 + j] for j in range(n2)]
    R2 = [array2[middle + 1 + j] for j in range(n2)]
    R3 = [array3[middle + 1 + j] for j in range(n2)]
    R4 = [array4[middle + 1 + j] for j in range(n2)]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L1[i] <= R1[j]:
            array1[k] = L1[i]
            array2[k] = L2[i]
            array3[k] = L3[i]
            array4[k] = L4[i]
            i += 1
        else:
            array1[k] = R1[j]
            array2[k] = R2[j]
            array3[k] = R3[j]
            array4[k] = R4[j]
            j += 1
        k += 1

    while i < n1:
        array1[k] = L1[i]
        array2[k] = L2[i]
        array3[k] = L3[i]
        array4[k] = L4[i]
        i += 1
        k += 1

    while j < n2:
        array1[k] = R1[j]
        array2[k] = R2[j]
        array3[k] = R3[j]
        array4[k] = R4[j]
        j += 1
        k += 1

# Try to open the data file
try:
    file_name = "data.dat"  # Assigns file_name to the name of the input file
    file_handle = open(file_name, 'r')  # Opens the file for reading
except FileNotFoundError:
    print("Error: File not found.")
    exit()

# Initialize lists to store data from the file
user_names = []
card_numbers = []
card_types = []
expiration_dates = []

# Reads all lines from the file
data_lines = file_handle.readlines()

# Removes the first line (header) from the list of lines
header_line = data_lines.pop(0)

# Processes each line in the file
for line in data_lines:
    given_name, surname, card_type, card_number, exp_month, exp_year = line.strip().split(',')

    # Combines the given name and surname into a full name
    full_name = f"{given_name} {surname}"
    user_names.append(full_name)

    card_types.append(card_type)  # Adds the credit card type to the list
    card_numbers.append(card_number)  # Adds the credit card number to the list

    # Format the month to ensure it has two digits
    if len(exp_month) == 1:
        exp_month = '0' + exp_month

    # Combines the year and month into an expiry date (as an integer)
    expiry_date = exp_year + exp_month
    expiration_dates.append(int(expiry_date))

# Closes the file after reading all data
file_handle.close()

# Sorts the lists based on expiration dates using merge sort
merge_sort(expiration_dates, user_names, card_numbers, card_types, 0, len(expiration_dates) - 1)

# Opens the output file for writing
result_file = open("output.txt", "w")

# Processes each credit card entry
for i in range(len(expiration_dates)):
    # Stops processing if the expiration date is beyond January 2025
    if expiration_dates[i] > 202501:
        break

    # Determines the status of the credit card (expired or needs renewal)
    status_text = "EXPIRED" if expiration_dates[i] < 202501 else "RENEW IMMEDIATELY"

    # Prints the formatted output to the console
    print(f"%-35s %-15s %-20s %-10s %-15s" % (user_names[i], card_types[i], card_numbers[i], expiration_dates[i], status_text))

    # Writes the formatted output to the file
    result_file.write(f"\n%-30s %-15s %-20s %-10s %-15s" % (user_names[i], card_types[i], card_numbers[i], expiration_dates[i], status_text))

# Closes the output file after writing all data
result_file.close()

# Automatically open the output file in the default text editor
import os
os.startfile('output.txt')
