# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

vowels = ["a","e","i","o","u"]

def count_vowels(word):
    number = 0
    for letter in word:
        if letter in vowels:
            number += 1
    return number



def test_challenge_01_happy_case(): 
     assert count_vowels('Kaleidoscope') == 6

