import math
# It takes 21 seconds to wash your hands
# and help prevent the spread of COVID-19.
#
# Create a function that takes the number of times 
# a person washes their hands per day (n) 
# and the number of months (m) they follow this routine, 
# and calculates the duration in minutes and seconds 
# that person spends washing their hands.
#
# Examples:
# wash_hands(8, 7) ➞ "588 minutes and 0 seconds"
# wash_hands(0, 0) ➞ "0 minutes and 0 seconds"
# wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
# 
# Notes: Consider a month has 30 days.

def wash_hands(n, m):
    amount = ((n*21)*30*m)
    min = math.floor(amount/60)
    sec = amount%60
    return f"{min} minutes and {sec} seconds"



def test_challenge_03_case_1():
    assert wash_hands(8, 7) == '588 minutes and 0 seconds'