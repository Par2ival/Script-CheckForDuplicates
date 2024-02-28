# Quick script to check if there are any duplicate SN in a list and return the values if so
# Author: Steve Elson
# Props: Google, mimo, My Mum

import pandas as pd

# import excel sheet of SN (SNs in 1 column with heading)
serial_raw = pd.read_excel("C:\data\Python\SerialNumbers.xlsx", usecols=[0])
# convert the SN column to a row
serial_raw = serial_raw.transpose()
# create an empty list to be populated later
serial_list = []

# loop to create a clean list of SN without index numbering
for serial in serial_raw.iloc[0]:
    serial_list.append(serial)

# creates a set from the previous list (duplicates cannot exist in a set)
serial_set = set(serial_list)

# Checks if there are the same numnber of SN in the set and list
if len(serial_list) == len(serial_set):
    print(f"There are no duplicate SNs")
    print(f"There are {len(serial_list)} unique SNs")
    print(serial_list)

# If there is a diff in legth, there must be at least 1 dupicate
else:
# sort lists in assending order
    serial_check_list = sorted(serial_list)
    serial_check_set = sorted(serial_set)
    index = 0
    duplicate = []

# check if the set serial matches the list SN in each index
    for serial in serial_check_set:
        if serial == serial_check_list[index]:
            index += 1
        else:
            duplicate.append(serial_check_list[index])
            index +=2

# effectivly checks if the last number in the list was a duplicate that got missed in the loop
    if len(duplicate) != len(serial_check_list) - len(serial_set):
        duplicate.append(serial_check_list[len(serial_check_list)-1])
 
    print(f"There is {len(serial_check_list) - len(serial_set)} duplicate SN, see list below:")
    print(f"{duplicate}")
