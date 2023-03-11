import sys

def evaluate_expression(expr):
    tokens = list(reversed(list(expr)))

    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ['+', '-', '*', '/']:
            a = stack.pop()
            b = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b) # use integer division

    return stack.pop()

if __name__ == '__main__':
    expr = sys.argv[1]


    result = evaluate_expression(expr)
    print(result)
