# Write a function in python that 
# takes an array of numbers and returns a
# sum of the square of all the numbers in the array.


###### Array???

def sum_of_squares(array_of_numbers):
    sum = 0
    for i in array_of_numbers:
        sum += i**2
    return sum


def test_challenge_06_happy_case(): 
     assert sum_of_squares([1,2,3,4]) == 30
