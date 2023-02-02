"""Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "4444444444444444", then it should return "4444"."""


# def credit_number_changer(card_number):
#     new_num = ""
#     rest_num = card_number.slice(-1,-4:1)
#     for num in card_number:
#         new_num *
#
#
#
#
# credit_number_changer(4444444444444444)

"""Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer."""

# def calculator(num_1 , calc_type, num_2):
#     if type(num_1) or type(num_2) != int:
#         return False
#     if calc_type == "+":
#         solution = num_1 + num_2
#     elif calc_type == "-":
#         solution = num_1 - num_2
#     elif calc_type == "/":
#         solution = num_1/num_2
#     elif calc_type == "*":
#         solution = num_1 * num_2
#     return solution


# Rebeccas:
def calculator(num1, operator, num2):
    num1 = int(num1)
    operator = str(operator)
    num2 = int(num2)
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '*':
        result = num1 * num2
    return result

#
# def calculate(instruction):
#     solution = 0
#     index = instruction.index("/")
#     num1 = instruction[index-1]
#     num2 = instruction[index+1]
#     between_sol = calculator(num1,"/", num2)
#     solution += between_sol
#
#     index = instruction.index("*")
#     num1 = instruction[index-1]
#     num2 = instruction[index+1]
#     between_sol = calculator(num1,"*", num2)
#     solution += between_sol
#
#     index = instruction.index("+")
#     num1 = instruction[index-1]
#     num2 = instruction[index+1]
#     between_sol = calculator(num1,"+", num2)
#     solution += between_sol
#
#     index = instruction.index("-")
#     num1 = instruction[index-1]
#     num2 = instruction[index+1]
#     between_sol = calculator(num1,"-", num2)
#     solution += between_sol
#     return solution

def calculate(instructions):
    operators = ["/", "*", "-","+"]
    for i in operators:
        index = instructions.index(i)
        instructions = calculator(instructions[index - 1], i, instructions[index + 1])

    return float(instructions)



#
#
# div_index = instructions.index("/") # input "3+2*2-1/1" -> index = 8
#     div_result = calculator(instructions[div_index-1], "/", instructions[div_index+1]) # instructions[div_index-1]- instructions[8-1]--> 1
#     # 1/1 = 1
#     # "3+2*2-1/1" --> input "3+2*2-1.0"
#     instructions = instructions.replace(instructions[div_index-1]+"/"+instructions[div_index+1], str(div_result))
#
#     print(instructions)
#
#     mult_index = instructions.index("*") # 3
#     mult_result = calculator(instructions[mult_index-1], "*", instructions[mult_index+1]) # 2 * 2 = 4
#     #  2*2=4
#     # "3+2*2-1.0" --> "3+4-1.0"
#
#     instructions = instructions.replace(instructions[mult_index-1]+"*"+instructions[mult_index+1], str(mult_result))
#
#     print(instructions)
#
#     sub_index = instructions.index("-")
#     sub_result = calculator(instructions[sub_index-1], "-", instructions[sub_index+1])
#     # 4-1 = 3
#     # "3+4-1.0" --> 3+3
#     instructions = instructions.replace(instructions[sub_index-1]+"-"+instructions[sub_index+1], str(sub_result))
#
#     print(instructions)
#
#     add_index = instructions.index("+")
#     add_result = calculator(instructions[add_index - 1], "-", instructions[add_index + 1])
#     # 4-1 = 3
#     # "3+4-1.0" --> 3+3
#     instructions = instructions.replace(instructions[add_index - 1] + "-" + instructions[add_index + 1],str(sub_result))
#
#     return instructions


def test_challenge_happy_case():
    assert calculator(3, "+", 5) == 8

def test_challenge_12_happy_case1():
    assert calculate("3+2*2-1/1") == 6.0