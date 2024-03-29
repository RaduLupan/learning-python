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
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data = elem)
                node = node.next

    def __iter__(self):
        # Enables traversal/iteration of a LinkedList in the most Pythonic way. Creating a method called traverse() would have not been Pythonic.
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        nodes.append("None")

        return " -> ".join(nodes)

arr=['1','2','3','4']
llist = LinkedList(nodes=arr)
print(llist)

for node in llist:
    print(node)

arr1 = [n for n in llist]
print(arr1)
