# The first part of the Python one is to make a function that:
# accepts an integer as input
# returns "fizz" if the integer is evenly divisible by 3
# returns "buzz" if the integer is evenly divisible by 5
# returns "fizzbuzz" if both are true
# returns the integer as a string if none of the above are true

# Did not incorporate a for loop
# Did not incorporate a range or xrange of numbers
# Did not think beyond what is above as it seemed you wanted me to be that literal
# and only work with the single interger that was entered so I did.



# print an explanation to console as to what this is all about.
print (" Welcome! \n If a number is divisible by 3 it will return Fizz. \n If it\'s divisible by 5 it will return Buzz. \n If it\'s divisible by both it will return FizzBuzz")
# ask for value input at console prompt
value = int(raw_input(" Please enter a number to see if its divisible by 3,5, or both: "))

# fizzbuzz function
def fizzbuzz(x):

    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif  x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

# print return value to console
print "\n" '{:>10}'.format(fizzbuzz(value))

