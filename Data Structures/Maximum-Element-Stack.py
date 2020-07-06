
# https://www.geeksforgeeks.org/find-maximum-in-a-stack-in-o1-time-and-o1-extra-space/

class Node:

    # Node Constructor
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    # Stack Constructor
    def __init__(self):
        self.top = None
        self.count = 0
        self.maximum = None

    def getMax(self):
        if self.top is None:
            return

        print (self.maximum)

    def push(self, val):

        # If Stack is empty, insert val into the stack and make maximum  = val
        # If stack is not empty, compare val and maximum. Two cases arise:
        #   If val is less than or equal to maximum, simply insert val
        #   If val is greater than maximum, insert (2 * val - maximum) into the stack and
        #           make maximum  = val    

        if self.top is None:
            self.top = Node(val)
            self.maximum = val
        
        elif val > self.maximum:
            temp = (2 * val) - self.maximum
            newNode = Node(temp)
            newNode.next = self.top
            self.top = newNode
            self.maximum = val
        else:
            newNode = Node(val)
            newNode.next = self.top
            self.top = newNode

    def pop(self):

        # If removed element is less than or equal to maximum, the maximum in the stack is still maximum
        # If removed element is greater than maximum, the maximum element now becomes (2 * maximum - removedElement)
        #   so update maximum as (2 * maximum - removedElement).

        if self.top is None:
            return
        
        removedNode = self.top.val
        self.top = self.top.next

        if removedNode > self.maximum:
            self.maximum = (2 * self.maximum) - removedNode
        else:
            return removedNode

stack = Stack()

cmds = {
    1: stack.push,
    2: stack.pop,
    3: stack.getMax
}

n = int(input())

for _ in range(n):

    query = list(map(int, input().split()))
    cmds[query[0]](*query[1:])