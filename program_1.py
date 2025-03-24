# Elijah Budd
# 3/24/2025
# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.
from fileinput import close


def count_file_lines():
    ######################
    try:
        with open('names.txt', 'r') as file:

            names = file.readlines()

            num_names = len(names)

            print(f'There are {num_names} names in the file')

            file.close()
            ######################
            print('In the count_file_lines function')

            return num_names

    except FileNotFoundError:
        print('File not found')

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
