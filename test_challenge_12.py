

# refactored code from class
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

def calculate(instructions):
    operators = ["/", "*", "-", "+"]
    for each_operator in operators:
        operator_index = instructions.index(each_operator)  # input "3+2*2-1/1" -> index = 8
        operator_result = calculator(instructions[operator_index - 1], each_operator,
                                instructions[operator_index + 1])  # instructions[div_index-1]- instructions[8-1]--> 1
        # 1/1 = 1
        # "3+2*2-1/1" --> input "3+2*2-1.0"
        instructions = instructions.replace(instructions[operator_index - 1] + each_operator + instructions[operator_index + 1],
                                            str(operator_result))

    return float(instructions)
