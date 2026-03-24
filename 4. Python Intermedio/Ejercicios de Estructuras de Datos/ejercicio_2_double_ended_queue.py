class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        current_node = new_node
        current_node.next = self.head
        while current_node.next is not None:
            current_node = current_node.next
        self.head = new_node

    def pop_left(self):
        if self.head:
            self.head = self.head.next
    
    def push_right(self, new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
    
    def pop_right(self):
        current_node = self.head
        while current_node.next is not None:
            next_node = current_node.next
            if next_node.next is not None:
                current_node = next_node
            else:
                current_node.next = None

first_node = Node("First")
my_double_e_queue = DoubleEndedQueue(first_node)
# my_double_e_queue
#.print_structure()
print("-"*30)
print("-> push_right")
second_node = Node("Second")
my_double_e_queue.push_right(second_node)

third_node = Node("Third")
my_double_e_queue.push_right(third_node)

forth = Node("Forth")
my_double_e_queue.push_right(forth)

my_double_e_queue.print_structure()

print("-"*30)
print("-> pop_left")
my_double_e_queue.pop_left()
my_double_e_queue.print_structure()

print("-"*30)
print("-> pop_right")
my_double_e_queue.pop_right()
my_double_e_queue.print_structure()

print("-"*30)
print("-> push_left")
my_double_e_queue.push_left(first_node)
my_double_e_queue.print_structure()