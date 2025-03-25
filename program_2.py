# Elijah Budd
# 3/25/2025
# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).
import random

def main():
    file = open('random.txt', 'w')

    while True:
        num_random = int(input('How many numbers do you want the file to hold(up to 1000)? '))

        if num_random > 1000:
            print('Too many numbers!')
            print('Try again!')
            continue

        if num_random <= 1000:
            for i in range(num_random):
                file.write(str(random.randint(1, 500)))
                file.write('\n')
            break

if __name__ == '__main__':
    main()
