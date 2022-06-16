from art import logo
print(logo)
# a simple calculator program
# the code is kinda ugly and can be improved more, but for now i will not update it
def calculator(f_number, s_number, operator):
    if operator == "+":
        answer = f_number + s_number
        print(f"{f_number} {operator} {s_number} = {answer}")
        return answer
    elif operator == "-":
        answer = f_number - s_number
        print(f"{f_number} {operator} {s_number} = {answer}")
        return answer
    elif operator == "*":
        answer = f_number * s_number
        print(f"{f_number} {operator} {s_number} = {answer}")
        return answer
    elif operator == "/":
        answer = f_number / s_number
        print(f"{f_number} {operator} {s_number} = {answer}")
        return answer
    else:
        return "wrong operation"



continue_from_previous = False
while True:

    if not continue_from_previous:
        first_number = float(input("What's the first number?: "))
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number?: "))
        output = calculator(first_number, second_number, operation)
        continue_calculation = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
    else:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number?: "))
        output = calculator(previous_value, second_number, operation)
        continue_calculation = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()

    if continue_calculation == "y":
        previous_value = output
        continue_from_previous = True
    elif continue_calculation == "n":
        continue_from_previous = False




