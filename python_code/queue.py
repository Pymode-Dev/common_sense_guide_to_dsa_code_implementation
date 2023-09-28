"""
Queue is also an abstract data type that follows the First-In-First-Out order system.
The Insertion[Enqueue] occurs at the end while Deletion[Dequeue] occurs at the front of the queue.
Backend Data Structure: list
"""

from typing import Any


class Queue:
    """
    class:
        Queue
        method: enqueue - add a new element to the end of the queue
                dequeue - remove an element at the front of the queue
    """
    def __init__(self):
        self.queue: list = []

    def enqueue(self, element: Any) -> None:
        self.queue.append(element)

    def dequeue(self) -> Any:
        return self.queue.pop(0)

    def read(self) -> Any:
        return self.queue[0]
