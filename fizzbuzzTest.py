# Enter the same number at each prompt to see if the funcitons work the same.

import unittest

class TestStringMethods(unittest.TestCase):

    def test_fizzbuzz(self):
        x = int(raw_input("Please enter a number to see if its divisible by 3,5, or both: "))
        result = ''
        if x % 3 == 0:
            result += "Fizz"
        if x % 5 == 0:
            result += "Buzz"
        if result == '': 
            result += str(x)  

        value = int(raw_input("Please enter a number to see if its divisible by 3,5, or both: "))
        def fizzbuzz(x):

            if x % 15 == 0:
                return "FizzBuzz"
            elif x % 3 == 0:
                return "Fizz"
            elif  x % 5 == 0:
                return "Buzz"
            else:
                return str(x) 

        self.assertEqual(result, (fizzbuzz(value))) 

if __name__ == '__main__':
    unittest.main()
