#!/usr/bin/python3
"""
This module defines linked lists
"""


class Node:
    """
    Defines a node
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines siglylinkedlist
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            current = self.__head
            pre = None
            while current and value > current.data:
                pre = current
                current = current.next_node
            if current is None:
                pre.next_node = Node(value)
            elif current is self.__head and pre is None:
                self.__head = Node(value, current)
            else:
                newNode = Node(value, current)
                pre.next_node = newNode

    def __repr__(self):
        node = self.__head
        txt = ''
        while node is not None:

