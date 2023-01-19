# A palindrome is a number/string that is same 
# forwards and backwards. 
# For example 545, 151, 34543, 343, 171, 48984 are palindrome. 
# A string like LOL, MADAM are also palindromes. 
# Write a function that takes an variable and returns 
# True or False if the variable is a palindrome.

def is_palindrome(var):
    new_var = str(var)
    len_var = len(new_var)
    for i in range(0,(len_var-1)):
        if new_var[i] == new_var[(-(i+1))]:
            return True
        else:
            return False








def test_challenge_04_palindrome_number():
    assert is_palindrome(545) == True

def test_challenge_04_palindrome_string():
    assert is_palindrome('MADAM') == True    