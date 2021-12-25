class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        # initialize Node with value, and next being None

class LinkedList:
    def __init__(self, head = None):
        # initialize Linked List by initializing head
        self.head = Node()
    
    def get_head(self):
        # return head of the Linked List
        current_node = self.head
        current_node = current_node.next
        return current_node.value

    def insert_back(self, node):
        # insert node to the back of the Linked List
        node1 = Node(node)
        while self.head.next is not None:
            self.head = self.head.next
        self.head.next = node1

    def get_last(self):
        # return last node of the Linked List
        while self.head.next is not None:
            self.head = self.head.next
        return self.head.value

    def get_list(self):
        # create list and append every value of Linked List to it.
        # return the list
        lst = []
        while self.head:
            lst.append(self.head.value)
            self.head = self.head.next
        return lst


my_list = LinkedList()

my_list.head = Node("Mon")
