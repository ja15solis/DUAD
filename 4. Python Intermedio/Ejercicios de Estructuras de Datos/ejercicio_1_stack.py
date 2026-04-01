class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    head: Node

    def __init__(self):
        self.head = None

    def print_structure(self):
        current_node = self.head
        if not current_node:
            print("Empty Deque")
            return
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        current_node = new_node
        current_node.next = self.head
        #not needed because the nodes are already connected 
        #while current_node.next is not None:
            #current_node = current_node.next
        self.head = new_node

    def pop(self):
        if self.head:
            self.head = self.head.next


my_stack = Stack()
first_node = Node("First")
my_stack.push(first_node)
# my_stack.print_structure()

second_node = Node("Second")
my_stack.push(second_node)

third_node = Node("Third")
my_stack.push(third_node)

forth = Node("Forth")
my_stack.push(forth)

my_stack.print_structure()

print("-> POP")

my_stack.pop()
my_stack.print_structure()

print("-> POP")

my_stack.pop()
my_stack.print_structure()

print("-> POP")

my_stack.pop()
my_stack.print_structure()

print("-> POP")

my_stack.pop()
my_stack.print_structure()

