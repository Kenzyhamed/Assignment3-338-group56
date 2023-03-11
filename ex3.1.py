import sys

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        return value

    def is_empty(self):
        return self.head is None

def evaluate(expression):
    stack = Stack()
    tokens = expression.split()
    for token in reversed(tokens):
        if token.isdigit():
            stack.push(int(token))
        elif token in ["+", "-", "*", "/"]:
            if stack.is_empty():
                raise Exception("Invalid expression")
            arg1 = stack.pop()
            if stack.is_empty():
                raise Exception("Invalid expression")
            arg2 = stack.pop()
            if token == "+":
                stack.push(arg1 + arg2)
            elif token == "-":
                stack.push(arg1 - arg2)
            elif token == "*":
                stack.push(arg1 * arg2)
            elif token == "/":
                stack.push(arg1 / arg2)
        elif token[0] == "(":
            stack.push(token[1:])
        elif token[-1] == ")":
            if stack.is_empty():
                raise Exception("Invalid expression")
            arg1 = stack.pop()
            operator = stack.pop()
            if operator != token[-2]:
                raise Exception("Invalid expression")
            stack.push(arg1)
        else:
            raise Exception("Invalid token")
    if stack.is_empty():
        raise Exception("Invalid expression")
    result = stack.pop()
    if not stack.is_empty():
        raise Exception("Invalid expression")
    return result

if __name__ == "__main__":
    expression = sys.argv[1]
    result = evaluate(expression)
    print(result)
