#!/usr/bin/python3
"""Define node for a singly-linked list."""


class Node:
    """Represents a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new node.
            next_node (Node): The next node to the new Node.
        """
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Retrieve the new node."""
        return (self._data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Retrieve the next_node of the Node."""
        return (self._next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initialize attribute head."""
            
        self._head = None

    def sorted_insert(self, value):
        """Insert a new Node to the Singly linked list.

        The node is inserted into the list at the correct
        sorted position.

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        elif value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return the printable representation of the single linked list."""
        if self._head is None:
            return ("Empty List")
        current = self._head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return (result)
