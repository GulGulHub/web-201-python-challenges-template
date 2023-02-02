""" # Tip calculator Create a Tip calculator (or rather a function for a tip calculator)!
 For any number of guests sharing a restaurant bill, calculate how much tip each guest needs to pay.
Use variables to store the number of guests, the amount of the bill and the tip in percentage, e.g.
        guest = 2;
        bill = 80;
        tipPercentage = 10;
Create a function which takes these values as input and outputs the total amount each guest needs to pay as well as the amount of tip that is included, eg `Each guest needs to pay: 44 euro` and `The amount of tip for each guest is: 4 euro`. """


guests = 2
bill = 80
tax_percentage = 10

def tip_calculator(guest_var, bill_var, tax_var):
    """this function calculates the amount + tip for each person sharing a bill"""
    if type(guest_var) != int or type(bill_var) != int or type(tax_var) != int:
        return "This is not a valid input. Please only enter int or floats"
    elif guest_var < 0 or bill_var < 0 or tax_var < 0:
        return "Invalid input - please only enter positive numbers"
    else:
        tip = (bill * tax_var/100)
        amount_each = (bill + tip)/2
        tip_each = tip / guest_var
        return f"Each guest needs to pay: {round(amount_each)} euro.\n The amount of tip for each guest is: {round(tip_each)} euro"

#without tests - functioncall:
# tip_calculator(guests, bill, tax_percentage)

def test_challenge_happy_case():
    assert tip_calculator(2,80,10) == f"Each guest needs to pay: 44 euro.\n The amount of tip for each guest is: 4 euro"

def test_challenge_sad_case_1():
    assert tip_calculator(2,"21",40) == "This is not a valid input. Please only enter int or floats"

def test_challenge_sad_case_2():
    assert tip_calculator(2,-4, 9) == "Invalid input - please only enter positive numbers"

# question - how do I test for Typeerror? raise Exceptions?
#def test_challenge__very_sad_case():
    #assert tip_calculator() == "Type Error"
