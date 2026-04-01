class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:   
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

#Test
third_node = Node("I'm the third")
second_node = Node("I'm the second", third_node)
first_node = Node("I'm the first node", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()