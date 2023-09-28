"""
This is an exercise that uses Stack to reverse a string
"""

from stack import Stack


def reverse_string(string: str) -> str:
    """
    This function reverse a string using Stack as the backend code.
    Args: 
        string - the string to reverse
    Return:
        str
    """
    stack = Stack()
    new_string = ""
    for i in string:
        stack.push(i)

    while len(stack.stack) != 0:
        new_string += stack.pop()

    return ''.join(new_string)
