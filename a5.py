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
        m = l + (r - l) // 2
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
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
    n1 = m - l + 1
    n2 = r - m

    L, L2, L3, L4 = [arr[l + i] for i in range(n1)], [arr2[l + i] for i in range(n1)], [arr3[l + i] for i in range(n1)], [arr4[l + i] for i in range(n1)]
    R, R2, R3, R4 = [arr[m + 1 + j] for j in range(n2)], [arr2[m + 1 + j] for j in range(n2)], [arr3[m + 1 + j] for j in range(n2)], [arr4[m + 1 + j] for j in range(n2)]

    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k], arr2[k], arr3[k], arr4[k] = L[i], L2[i], L3[i], L4[i]
            i += 1
        else:
            arr[k], arr2[k], arr3[k], arr4[k] = R[j], R2[j], R3[j], R4[j]
            j += 1
        k += 1

    while i < n1:
        arr[k], arr2[k], arr3[k], arr4[k] = L[i], L2[i], L3[i], L4[i]
        i += 1
        k += 1

    while j < n2:
        arr[k], arr2[k], arr3[k], arr4[k] = R[j], R2[j], R3[j], R4[j]
        j += 1
        k += 1

try:
    filename = "data.dat"
    fh = open(filename, 'r')
except FileNotFoundError:
    print("Error: File not found.")
    exit()

names, cc_nums, cc_types, expiry_dates = [], [], [], []
lines = fh.readlines()
first_line = lines.pop(0)
for line in lines:
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    name = f"{given_name} {surname}"
    names.append(name)
    cc_types.append(cc_type)
    cc_nums.append(cc_number)
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    expiry_date = exp_yr + exp_mo
    expiry_dates.append(int(expiry_date))

fh.close()
mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)

output = open("output.txt", "w")
for i in range(len(expiry_dates)):
    if expiry_dates[i] > 202501:
        break
    expired_text = "EXPIRED" if expiry_dates[i] < 202501 else "RENEW IMMEDIATELY"
    print(f"%-35s %-15s %-20s %-10s %-15s" % (names[i], cc_types[i], cc_nums[i], expiry_dates[i], expired_text))
    output.write(f"\n%-30s %-15s %-20s %-10s %-15s" % (names[i], cc_types[i], cc_nums[i], expiry_dates[i], expired_text))

output.close()

import os
os.startfile('output.txt')
