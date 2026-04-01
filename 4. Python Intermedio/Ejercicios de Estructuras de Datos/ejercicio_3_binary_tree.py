class Node:
    data: str
    next: "Node"

    def __init__(self, data, first_child=None, second_child=None):
        self.data = data
        self.first_child = first_child
        self.second_child = second_child
class BinaryTree:   
    root: Node

    def __init__(self, root,first_child=None,second_child=None):
        self.root = root
        self.first_child = first_child
        self.second_child = second_child

    #print from left to right 
    def print_structure(self,current_node,level = 0):
        if current_node is None:
            return 
        else:
            if current_node.first_child:
                #level += 1 #for spaces --it doesn't work
                self.print_structure(current_node.first_child,level+1) #recursive function to print the first child node

            #print the current node to have the parent node or if it comes from a recursive function the child node
            print("\t"* level + current_node.data) 
            
            if current_node.second_child:
                #level += 1 #for spaces --it doesn't work
                self.print_structure(current_node.second_child,level+1) #recursive function to print the second child node

#Test
h_node = Node("H")
i_node = Node("I")
j_node = Node("J")
d_node = Node("D",h_node,i_node)
e_node = Node("E",j_node)
b_node = Node("B",d_node,e_node)
f_node = Node("F")
g_node = Node("G")
c_node = Node("C",f_node,g_node)
a_node = Node("A",b_node,c_node)


binary_tree = BinaryTree(a_node)
binary_tree.print_structure(a_node)