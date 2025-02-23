import numpy as np

# Linked Lists

# Singly Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.nextnode = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_start(self, newval):
        newnode = Node(newval)
        if self.head is None:
            self.head = newnode
        else:
            newnode.nextnode = self.head
            self.head = newnode

    def add_end(self, newval):
        newnode = Node(newval)
        if self.head is None:
            self.head = newnode
        else:
            curnode = self.head
            while curnode.nextnode:
                curnode = curnode.nextnode
            curnode.nextnode = newnode
    
    def print_ll(self):
        vals = []
        node = self.head
        while node.nextnode is not None:
            vals.append(node.val)
            node = node.nextnode
        vals.append(node.val)
        print(vals)

    # Reverse linked list
    def reverse_ll(self):

        curnode = self.head
        prevnode = None
        while curnode:
            nextnode = curnode.nextnode
            curnode.nextnode = prevnode
            prevnode = curnode
            curnode = nextnode
        self.head = prevnode

# Doubly Linked List
class nodedoub:
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None
        
class doublelist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_start(self, value):
        new_node = nodedoub(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.nextnode = temp
            new_node.prevnode = None
            
    def add_end(self, value):
        new_node = nodedoub(value)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            temp = self.tail
            temp.nextnode = new_node
            self.tail = new_node
            new_node.prevnode = temp
            new_node.nextnode = None
            
    def add_index(self, value, idx):
        new_node = nodedoub(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            i = 0
            current_node = self.head
            while i<idx-1 and current_node.nextnode:
                current_node = current_node.nextnode
                i += 1
            right_node = current_node.nextnode
            current_node.nextnode = new_node
            new_node.nextnode = right_node
            new_node.prevnode= current_node
            right_node.prevnode = new_node
                
    def del_node(self, idx):
        if self.head:
            i = 0
            current_node = self.head
            if idx==0:
                self.head = current_node.nextnode
            else:
                while i<idx-1 and current_node:
                    current_node = current_node.nextnode
                    i += 1
                target_node = current_node.nextnode
                right_node = target_node.nextnode
                current_node.nextnode = right_node
                right_node.prevnode = current_node
                target_node.nextnode = None
                target_node.prevnode = None

# Circular Linked List
class circlist:
    def __init__(self):
        self.head = None
        
    def add_start(self, value):
        new_node = node1(value)
        if not self.head:
            new_node.nextnode = new_node
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.nextnode = old_head
            temp = old_head
            while temp.nextnode!=old_head:
                temp = temp.nextnode
            temp.nextnode= new_node
            
    def print_circlist(self):
        if self.head:
            temp = self.head
            first_node = self.head
            print(first_node.value)
            while temp.nextnode != first_node:
                temp = temp.nextnode
                print(temp.value)
            
# Stack
# Check whether expression is balanced
def check_balanced(expr):
    explist = [c for c in expr.strip() if c!=" "]
    stacklist = []
    n = len(explist)
    
    if n%2==0:
        valid_ex=True
    else:
        valid_ex = False
        return valid_ex
    
    open_parens = ["(", "[", "{"] 
    close_parens = [")", "]", "}"] 
    for c in explist:
        if c in open_parens:
            stacklist.append(c)
        elif c in close_parens:
            lastchar = stacklist.pop()
            if (c==")" and lastchar!="(") or (c=="]" and lastchar!="[") or (c=="}" and lastchar!="{"):
                valid_ex=False
                return valid_ex
        else:
            valid_ex=False
            return valid_ex
        
    return valid_ex

# Queue
class que():
    def __init__(self):
        self.start = 0
        self.end = -1
        self.arr = []

    def enque(self, val):
        self.end += 1
        self.arr.insert(0, val)

    def deque(self):
        if self.end>-1:
            val = self.arr.pop()
            self.end = self.end-1
            return val
    

if __name__=='__main__':
    # Linked list
    ll = LinkedList()
    ll.add_start(1)
    ll.add_start(2)
    ll.add_end(10)
    ll.add_end(3)
    print("Original list:", end= " ")
    ll.print_ll()
    print("Reversed list:", end=" ")
    ll.reverse_ll()
    ll.print_ll()
    # Check whether expression is balanced
    expr = "[{(()}]"
    print(expr, " Balanced? ", check_balanced(expr))
    print(expr, " Balanced? ", expr.replace("()", "").replace("[]","").replace("{}","")=="")