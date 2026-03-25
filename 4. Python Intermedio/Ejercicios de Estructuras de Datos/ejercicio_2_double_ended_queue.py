class Node:
    data: str
    next: "Node"
    previous: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleEndedQueue:
    head: Node
    def __init__(self):
        self.head = None
        self.last = None

    def print_structure(self):
        current_node = self.head
        if not current_node:
            print("Empty Deque")
            return
        while current_node.next is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        current_node = new_node
        new_node.next = None
        new_node.previous = None
        if not self.head:
            self.head = current_node
            self.last = current_node
        else:
            current_node.next = self.head
            self.head.previous = current_node
            self.head = current_node

    def pop_left(self):
        if not self.head:
            return
        if self.head == self.last: #one element
            self.head = None
            self.last = None
        else:
            self.head = self.head.next
            self.head.previous = None
    
    def push_right(self, new_node):
        current_node = new_node
        new_node.next = None
        new_node.previous = None
        if not self.last:
            self.last = current_node
            self.head = current_node
        else:
            self.last.next = current_node
            current_node.previous = self.last
            self.last = current_node
    
    def pop_right(self):
        if not self.last:
            return
        if self.head == self.last: #one element
            self.head = None
            self.last = None
        else:
            self.last = self.last.previous
            self.last.next = None
my_double_e_queue = DoubleEndedQueue()
first_node = Node("First")
my_double_e_queue.push_right(first_node)
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
my_double_e_queue.push_left(first_node) ##I have to clear the next and previous nodes
my_double_e_queue.print_structure()