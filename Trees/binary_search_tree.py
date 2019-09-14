"""
- binary tree has up to two children

Basics for implementing binary search trees. 
- left subtree keys are less than the root value
- right subtree keys are greater than root value
- each left and right subtree is a BST

Operations and Runtimes: 
Search: avg O(logn), worst O(n)
Insert: avg O(logn), worst O(n)
Delete: avg O(logn), worst O(n)

worst case occurs when you have a spindly tree
"""

class Node():
    def __init__(self, value, left=None, right=None): 
        self.value = value
        self.left = left
        self.right = right

def search(root, value): 
    """
    Returns true if value is found in the BST
    """
    if root is None:
        return False
    if value < root.value:
        return search(root.left, value)
    elif value > root.value: 
        return search(root.right, value)
    else: 
        return True


def insert(root, value):
    """
    Insert a new node with value as its key 
    """
    if root is None: 
        root = Node(value)
    elif value < root.value:
        if root.left is None: 
            root.left = Node(value)
        else: 
            insert(root.left, value)
    elif value > root.value: 
        if root.right is None: 
            root.right = Node(value)
        else: 
            insert(root.right, value)


def delete(root, value):
    """
    Delete node with the given value as its key. 
    Must return a tree that still satisfies B tree properties. 

    Situation 1: node to be deleted is a leaf node
    - the node will be replaced with None

    Situation 2: node to be deleted has only one child
    - replace the node with its child and delete the child node

    Situation 3: node to be deleted has more than child
    - replace node with its in-order successor (smallest node in the right subtree)
      or with its in-order predecessor (greater node in the left subtree) recursively 
      until the node is a leaf of the B tree
        - in-order successor will always have null left child
    - replace the node that's now a leaf with None
    """
    if root is None: 
        return root
    if value < root.value:
        return delete(root.left, value)
    elif value > root.value: 
        return delete(root.right, value)
    else: 
        # node to delete has no children
        if root.left is None and root.right is None:
            if root.value == value:
                return None
            return root
        