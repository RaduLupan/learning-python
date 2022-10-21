'''
Reference:
https://realpython.com/linked-lists-python/
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        nodes.append("None")

        return " -> ".join(nodes)

llist = LinkedList()
print(llist)

node1=Node('a')
llist.head=node1
print(llist)

node2=Node('b')
node1.next = node2

node3=Node('c')
node2.next = node3
print(llist)
