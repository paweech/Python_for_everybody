#Python for everybody Course 1 Exercise 2.3

# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number.

# This first line is provided for you
# Desired result = "Pay: 96.25"

hrs = input("Enter Hours:")
rate = input ("Enter rate per hour: ")
gpay = float(hrs) * float(rate)
print("Pay: ", gpay)

#Run the program and input the numbers!
