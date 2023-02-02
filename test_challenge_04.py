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

def calculate(instruction):
    solution = 0
    if "*" in instruction:
        index = instruction.index("*")
        num1 = instruction[index-1]
        num2 = instruction[index+1]
        between_sol = calculator(num1,"*", num2)
        solution += between_sol
    elif "/" in instruction:
        index = instruction.index("/")
        num1 = instruction[index-1]
        num2 = instruction[index+1]
        between_sol = calculator(num1,"/", num2)
        solution += between_sol
    elif "+" in instruction:
        index = instruction.index("+")
        num1 = instruction[index-1]
        num2 = instruction[index+1]
        between_sol = calculator(num1,"+", num2)
        solution += between_sol
    elif "-" in instruction:
        index = instruction.index("-")
        num1 = instruction[index-1]
        num2 = instruction[index+1]
        between_sol = calculator(num1,"-", num2)
        solution += between_sol
    return solution

calculate("3+2*2-1/1")
