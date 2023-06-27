#!/usr/bin/python3
"""Defines classes for a singly-linked list."""

class Node:
    """This class represents a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data value to be stored in the Node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of the Node."""
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("The data value must be an integer.")
        self._data = value

    @property
    def next_node(self):
        """Get or set the next_node of the Node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("The next_node must be a Node object.")
        self._next_node = value

class SinglyLinkedList:
    """This class represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self._head = None

    def sorted_insert(self, value):
        """Insert a new Node into the SinglyLinkedList.

        The Node is inserted at the correct position in ascending order.

        Args:
            value (Node): The new Node to be inserted.
        """
        new_node = Node(value)

        if self._head is None:
            new_node.next_node = None
            self._head = new_node
        elif self._head.data > value:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return the string representation of the SinglyLinkedList."""
        values = []
        current = self._head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)

