"""
This is the code implementation for stack data structure.
Stack is an abstract data type that follows the Last-In-First-Out order system.
Both Insertion[Push] and Deletion[Pop] occur at the end of the stack.
Backend Data Structure: List
"""

from typing import Any


class Stack:
    """
    class:
        Stack
        method:
            push: add a new element
            pop: remove the last element to add
    """
    def __init__(self) -> None:
        """
        Initialize the backend data structure.
        """
        self.stack: list = []

    def push(self, element) -> None:
        """
        Add a new element to the end of the stack.
        Args:
            element: Any
        Return:
            None
        """
        self.stack.append(element)

    def pop(self) -> Any:
        """
        Remove the last element to add at the end of the stack.
        Args:
            None
        Return:
            Any
        """
        return self.stack.pop()

    def read(self) -> Any:
        """
        Read the last element to add to the stack.
        Args:
            None
        Return:
            Any
        """
        return self.stack[-1]
