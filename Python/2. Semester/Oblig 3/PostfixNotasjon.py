# Funksjonen tar et infiksuttrykk som input og returnerer et postfix-uttrykk.
# Eksempel: (6-9)*(3+4)^2 => 6 9 - 3 4 + 2 ^ *
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operator_stack = []
    output_stack = []
    
    for char in expression:
        if char.isnumeric():
            output_stack.append(char)  # Bruker append for liste

        elif char == ' ':
            continue  # Ignorer mellomrom
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_stack.append(operator_stack.pop())  # Bruker append for liste

            operator_stack.pop()  # Remove '(' from operator_stack
        else:
            while operator_stack and operator_stack[-1] != '(' and precedence[char] <= precedence[operator_stack[-1]]:
                output_stack.append(operator_stack.pop())  # Bruker append for liste

            operator_stack.append(char)

    while operator_stack:
        output_stack.append(operator_stack.pop())  # Bruker append for liste

    return ' '.join(output_stack)  # Konverterer liste til string

def eval_postfix(postfix_expression):
    evaluation_stack = []
    tokens = postfix_expression.split()
    for token in tokens:
        if token.isnumeric():
            evaluation_stack.append(token)
        else:
            operand2 = evaluation_stack.pop()
            operand1 = evaluation_stack.pop()
            evaluation_stack.append(str(eval(operand1 + token + operand2)))
    return evaluation_stack[0]

# Eksempel på bruk
expressions = ["(1 + 2) * 3", " 2 * 3 - 4 + 8 * 2","(6-9)*(3+4)^2"]
for expression in expressions:
    postfix_expression = infix_to_postfix(expression)
    result = eval_postfix(postfix_expression)
    print("infix-uttrykk :", expression , " blir postfix-uttrykk:", postfix_expression, " og resultatet er:", result)
  