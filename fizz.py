x = int(raw_input("Please enter the number to FizzBuzz up to: "))
result = ''
if x % 3 == 0:
    result += "Fizz"
if x % 5 == 0:
    result += "Buzz"
if result == '': 
    result += str(x)   
print result 