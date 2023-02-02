"""Write a Python program that calculates the area of a circle based on the radius entered by the user."""
import math
def calc_area(radius):
    if radius < 0:
        return "negative radius not possible"
    else:
        area = math.pi * (radius ** 2)
        return round(area, 2)


    # try:
    #     area = math.pi * (radius**2)
    # except TypeError:
    #     return "invalid input"
    # else:
    #     return round(area,2)


def test_challenge_00_happy_case():
    assert calc_area(2) == 12.57

def test_challenge_01_idiot_case():
    assert calc_area(-56) == "negative radius not possible"


