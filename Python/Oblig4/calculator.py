class Calculator:
    def __init__(self):
        self.log = []

    def calculate(self, operand1, operand2, operator):
        # Evaluate based on operator and append to log
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            if operand2 != 0:
                result = operand1 / operand2
            else:
                result = "Undefined"  # Division by zero handling
        else:
            result = "Invalid Operator"

        expression = f"{operand1} {operator} {operand2} = {result}"
        self.log.append(expression)
        return result

    def get_log(self):
        return self.log

    def get_last_logged(self):
        return self.log[-1] if self.log else "No calculations yet."

    def clear_log(self):
        self.log.clear()
