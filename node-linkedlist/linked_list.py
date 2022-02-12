class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        # initialize Node with value, and next being None

class LinkedList:
    def __init__(self):
        # initialize Linked List by initializing head
        self.head = Node()
    
    def get_head(self):
        # return head of the Linked List
        current_node = self.head
        current_node = current_node.next
        return(current_node.value)

    def insert_back(self, node):
        # insert node to the back of the Linked List
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while (last_node.next):
            last_node = last_node.next
        last_node.next = new_node

    def get_last(self):
        # return last node of the Linked List
        cur_node = self.head
        while cur_node.next is not None:
        	cur_node = cur_node.next
        return(cur_node.value)

    def get_list(self):
        # create list and append every value of Linked List to it.
        # return the list
        lst = []
        node0 = self.head
        while node0 is not None:
            lst.append(node0.value)
            # print(node0.value)
            node0 = node0.next
        return lst


# my_list = LinkedList()

# my_list.head = Node("a")
# my_list.insert_back("abc")
# my_list.insert_back("abc1")
# my_list.insert_back("def")
# my_list.insert_back("def2")
# print(my_list.get_head())
# print(my_list.get_last())
# print(my_list.get_list())