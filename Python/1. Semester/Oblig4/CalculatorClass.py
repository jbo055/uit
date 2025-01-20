class Calculator:
    def __init__(self):
        self.log = []

    def calculate(self, operand1, operand2, operator):
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                result = "Division by zero"
            else:
                result = operand1 / operand2
        else:
            result = "Invalid operator"
        self.log.append(f"{operand1} {operator} {operand2} = {result}")
        return result
    
    def get_log(self):
        return self.log
    
    def get_last_logged(self):
        return self.log[-1] if self.log else "No log entries"
    
    def clear_log(self):
        self.log.clear()

