# Elijah Budd
# 3/28/2025
# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.
# The program should handle the following exceptions:
# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.
def sum_numbers_from_file():
    ######################
    subtotal = 0
    file = open('numbers.txt', 'r')

    try:
        for number in file:
            subtotal += int(number)

        print('The total is', subtotal)
        file.close()

    except IOError:
        print('An error occurred trying to read the file.')
    except ValueError:
        print('Non-numeric data found in the file.')
    except:
        print('An error occurred.')
        ######################
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
