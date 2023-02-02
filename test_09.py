"""Write a Python program that concatenates all elements in a list into a string and returns it.
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20."""

def concat_list(list):
    new_string = "".join(map(str,list))
    return str(new_string)

def test_challenge_01_happy_case():
    shopping_list = [3,4,5,6]
    assert concat_list(shopping_list) == "3456"

def test_challenge_07_happy_case_2():
    shopping_list = ["a", "b", "c"]
    assert concat_list(shopping_list) == "abc"




