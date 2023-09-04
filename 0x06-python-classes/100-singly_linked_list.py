#!/usr/bin/python3
"""Define a class for a singly-linked list."""


class Node:
    """Represents node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initiate a new Node.

        Args:
            data (int): The new Node data.
            next_node (Node): The next node after the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrive Node data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initiate a new Singly Linked List."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new Node to the Singly Linked List.

        The node is inserted into the list at the sorted
        numerical position.

        Args:
            value (Node): The Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Return the printable representation of the single linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
