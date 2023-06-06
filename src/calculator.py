class Calculator:
    def __init__(self):
        self.clear()

    # Clear or reset the calculator to its initial state.
    def clear(self):
        self.current = 0  # the current value to be displayed on the calculator
        self.pending_operation = None  # the operation that is yet to be performed
        self.pending_value = None  # the value that is yet to be used in the operation
        self.last_input_was_operator = False  # flag to indicate if the last input was an operator

    # Handle the input command and perform the appropriate operation.
    def input(self, command):
        # Replace the operator symbols with spaces around them so that they can be easily split into tokens
        command = command.replace('+', ' + ')
        command = command.replace('-', ' - ')
        command = command.replace('*', ' * ')
        command = command.replace('/', ' / ')
        command = command.replace('=', ' = ')
        tokens = command.split()

        temp_tokens = []
        last_token = ""

        # handle consecutive operators, e.g. ++2 or +--5
        for token in tokens:
            if token in ['+', '-'] and last_token in ['+', '-']:
                temp_tokens.pop()  # remove the last operator

                # if the operators are different, it's equivalent to a single '-' operator
                # if they are the same, it's equivalent to a single '+' operator
                if (token == '-' and last_token == '+') or (token == '+' and last_token == '-'):
                    temp_tokens.append('-')
                else:
                    temp_tokens.append('+')
            else:
                temp_tokens.append(token)

            last_token = token  # update the last_token

        tokens = temp_tokens  # update the tokens

        for token in tokens:
            if token == '=':  # if the token is '=', perform the pending operation
                if self.pending_operation and self.pending_value is not None:
                    self.current = self.perform_operation(self.pending_operation, self.current, self.pending_value)
                    self.pending_operation = None
                    self.pending_value = None
                    self.last_input_was_operator = False
            elif token in ['+', '-', '*', '/']:  # if the token is an operator, update the pending operation
                if self.pending_operation and self.pending_value is not None:
                    self.current = self.perform_operation(self.pending_operation, self.current, self.pending_value)
                    self.pending_value = None
                self.pending_operation = token
                self.last_input_was_operator = True
            elif token == 'c':  # if the token is 'c', clear the calculator
                self.clear()
            elif token == '!':  # if the token is '!', negate the current value
                self.current *= -1
            else:  # if the token is a number, update the current value or the pending value
                try:
                    value = int(token)
                    if self.last_input_was_operator:
                        self.pending_value = value
                        self.current = self.perform_operation(self.pending_operation, self.current, self.pending_value)
                        self.pending_value = None
                    else:
                        self.current = value
                    self.last_input_was_operator = False
                except ValueError:
                    raise ValueError(f"Invalid token: {token}")
        return self.current

    @staticmethod
    def perform_operation(operation, operand1, operand2):
        if operation == '+':
            return operand1 + operand2
        elif operation == '-':
            return operand1 - operand2
        elif operation == '*':
            return operand1 * operand2
        elif operation == '/':
            if operand2 == 0:
                raise ValueError("Cannot divide by zero")
            return operand1 / operand2
