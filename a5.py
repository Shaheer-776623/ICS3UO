"""
Author : Shaheer Mallick
Student Number: 776623
Revision date : 20 Jan 2025
Program : Credit Card Report
Description : Report of all credit cards in the customer database that have expired.
Variable Dictionary:
    filename: str - Name of the file
    fh: file object - File handle
    names: list - List of names (first and last)
    cc_nums: list - List of credit card numbers
    cc_types: list - List of credit card types
    expiry_dates: list - List of expiry dates
    lines: list - List of all the lines in file
    first_line: str - First line of the file (to be removed from lines)
    output_file: file object - File handle for the output file
    expired_text: str - Text to display when expired
"""

def mergeSort(arr, arr2, arr3, arr4, l, r):
    """
    Function to perform merge sort on two arrays.
    Parameters:
        arr (list): Array to be sorted.
        arr2, arr3, arr4 (list): Other arrays to be sorted.
        l (int): Left index of the subarray.
        r (int): Right index of the subarray.
    """
    if l < r:
        # Finds the middle index of the array
        m = l + (r - l) // 2

        # Recursively sorts the left half of the array
        mergeSort(arr, arr2, arr3, arr4, l, m)

        # Recursively sorts the right half of the array
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)

        # Merges the two sorted halves
        merge(arr, arr2, arr3, arr4, l, m, r)

def merge(arr, arr2, arr3, arr4, l, m, r):
    """
    Function to merge two sorted arrays.
    Parameters:
        arr (list): Array to be sorted.
        arr2, arr3, arr4 (list): Other arrays to be sorted.
        l (int): Left index of the subarray.
        m (int): Middle index of the subarray.
        r (int): Right index of the subarray.
    """
    # Calculates the sizes of the two subarrays
    n1 = m - l + 1
    n2 = r - m

    # This creates temporary arrays to hold data for the left and right subarrays
    L = [arr[l + i] for i in range(n1)]
    L2 = [arr2[l + i] for i in range(n1)]
    L3 = [arr3[l + i] for i in range(n1)]
    L4 = [arr4[l + i] for i in range(n1)]

    R = [arr[m + 1 + j] for j in range(n2)]
    R2 = [arr2[m + 1 + j] for j in range(n2)]
    R3 = [arr3[m + 1 + j] for j in range(n2)]
    R4 = [arr4[m + 1 + j] for j in range(n2)]

    # Initializes variables for the left, right, and merged subarrays
    i = j = 0
    k = l

    # Merges data back into the original arrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            # Copies data from the left subarray if it's smaller or equal
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            # Copies data from the right subarray if it's smaller
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1

    # Copies any remaining elements from the left subarray
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1

    # Copies any remaining elements from the right subarray
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Trys opening the data file
try:
    filename = "data.dat"  # Assigns filename to the name of the input file
    fh = open(filename, 'r')  # Opens the file for reading
except FileNotFoundError:
    # Prints an error message and exit if the file is not found
    print("Error: File not found.")
    exit()

# Initialize lists to store data from the file
names = []
cc_nums = []
cc_types = []
expiry_dates = []

# Reads all lines from the file
lines = fh.readlines()

# Removes the first line (header) from the list of lines
first_line = lines.pop(0)

# Processes each line in the file
for line in lines:
    # Splits the line into individual components that was specified in the first line
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')

    # Combines the given name and surname into a full name
    name = f"{given_name} {surname}"
    names.append(name)  # Adds the name to the list of names

    cc_types.append(cc_type)  # Adds the credit card type to the list
    cc_nums.append(cc_number)  # Adds the credit card number to the list

    # Format the month to ensure it has two digits
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo

    # Combines the year and month into an expiry date (as an integer)
    expiry_date = exp_yr + exp_mo
    expiry_dates.append(int(expiry_date))

# Closes the file after reading all data
fh.close()

# Sorts the lists based on expiry dates using merge sort
mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)

# Opens the output file for writing
output = open("output.txt", "w")

# Processes each credit card entry
for i in range(len(expiry_dates)):
    # Stops processing if the expiry date is beyond January 2025
    if expiry_dates[i] > 202501:
        break

    # Determines the status of the credit card (expired or needs renewal)
    expired_text = "EXPIRED" if expiry_dates[i] < 202501 else "RENEW IMMEDIATELY"

    # Prints the formatted output to the console
    print(f"%-35s %-15s %-20s %-10s %-15s" % (names[i], cc_types[i], cc_nums[i], expiry_dates[i], expired_text))

    # Writes the formatted output to the file
    output.write(f"\n%-35s %-15s %-20s %-10s %-15s" % (names[i], cc_types[i], cc_nums[i], expiry_dates[i], expired_text))

# Closes the output file after writing all data
output.close()

# Automatically open the output file in the default text editor
import os
os.startfile('output.txt')
