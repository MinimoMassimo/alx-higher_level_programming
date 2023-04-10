#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node
    @property
    def data(self):
        return self.__data
    @property
    def next_node(self):
        return self.__next_node
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) or value is None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        """
        String representation of singly linked list so it is printable
        """
        string = ""
        temp = self.__head
        while tmp is not None:
            string += str(temp.data())
            temp = temp.next_node()
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        if self.__head is None:
            self.__head = Node(value)
        else:
            temp = Node(value)
            if self.__head.data > value:
                temp.next_node(self.__head)
                self.__head = temp
            elif self.__head.data < value:
                while self.__head.next_node is not None and self.__head.next_node.data < value:
                    self.__head = self.__head.next_node()
                temp.next_node = self.__head.next_node()
                self.__head.next_node(temp)
