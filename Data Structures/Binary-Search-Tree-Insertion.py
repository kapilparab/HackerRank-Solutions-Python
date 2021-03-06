class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

    def insert(self, val):

        node = Node(val)

        if self.root is None:
            self.root = node

        # The reason self.root doesnt work when directly specified is because self is a
        # BinarySearchTree object and not a node object. Traversing using self.root
        # assigns new values to the whole Tree.
        # Using the next line we pull the top node of the Tree.

        current = self.root
        while True:
            if val > current.info:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    break
            elif val < current.info:
                if current.left:
                    current = current.left
                else:
                    current.left = node
            else:
                break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
