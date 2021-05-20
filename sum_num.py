#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 20, 2021
# This program determines the sum of the users num plus
# all the numbers preceding it down to 0


# get user num and reset the variables (only necessary
# if making a loop)
user_num = input("what is your number: ")
total = 0
counter = 0

# make sure the users num can be an integer
try:
    user_num = int(user_num)

    # check if that number is > or = 0
    if (user_num >= 0):

        # this is the while loop it adds to the counter
        # preventing infini loop and increases the total by
        # the counter every time the program is repeated
        while (counter < user_num):
            counter = counter + 1
            total = total + counter

        # after done print the total
        print(total)
    # if the number was below 0
    else:
        print("This is not a positive number")

# if the number the user inputed was not a number
except ValueError:
    print("This is not a valid input")
