class Node:
    def __init__(self, value = None, left = None, right = None):
        # initiate value, left node, and right node
        self.left = left
        self.right = right
        self.value = value

class BSTSet:
    def __init__(self, root = None):
        # initiate root
        self.root = root
        
    def insert(self, value):
        # insert a node with value to the binary search tree according to the rule of BST
        if self.root == None:
            self.root = Node(value)
        else:
            if value < self.root:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.insert(value, self.left)
            elif value > self.root:
                if self.right == None:
                    self.right = Node(value)
                else:
                    self.insert(value, self.right)


    def get_min(self):
        # if there are no elements in BST, return "BSTSet is empty"
        # otherwise return value that is minimal in the BST
        if self.root == None:
            return "BSTSet is empty"
        else:
            return self.left

    def get_max(self):
        # # if there are no elements in BST, return "BSTSet is empty"
        # otherwise return value that is maximal in the BST
        if self.root == None:
            return "BSTSet is empty"
        else:
            return self.right
        
    def is_in_bstset(self, value):
        # return true if value exists in the nodes of BST
        # otherwise return false
        if value == self.root:
            return True
        else:
            if value == self.left or value == self.right:
                return true
            else:
                return False

        

def reverse_tree(root):
    # reverse tree
    # reversing means that if node has left child, it will become right child, and vice versa