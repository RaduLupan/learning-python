'''
Problem: Reverse a Linked List in Groups of Given Size
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed
(See Example 2 for clarification).

Example 1:
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.

Example 2:
Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4 
Explanation: 
The first 3 elements are 1,2,3 are reversed 
first and then elements 4,5 are reversed.Hence, 
the resultant linked list is 3->2->1->5->4.

Reference:
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1?page=3&company[]=Amazon&sortBy=submissions
https://realpython.com/linked-lists-python/
'''

#--------------------------------------------------------------------------------------------------------
# In part 1 we solved a simplified version of the problem when the list to be reversed is a simple array. 
# In part 2 we will apply this solution to solve the original problem of reversing a linked list.
#--------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None

        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data = elem)
                node = node.next

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")

        return " -> ".join(nodes)

def reverse_list(arr, k):
    '''
    Reverses a list in groups of k elements. If the length of the list is not multiple of k then the remainder group is also reversed.
    '''
    n = len(arr)
    result = []

    # If n is multiple of k, the number of groups with k elements is g = n // k and the remainder group has r = 0 elements.
    if n % k == 0:
        g = n//k
        r = 0

    # If n is not multiple of k, the number of groups with k elements is g = (n-1) // k and the remainder group has r = n % k elements.
    else:
        g = (n-1)//k
        r = n % k

    for i in range(g):
        # Appends all k elements of the group to the result list in reverse order.
        for j in range((i+1)*k-1, i*k-1, -1):
            result.append(arr[j])
    
    if r != 0:
        # Appends all elements of the remainder group (less than k) to the result list in reverse order.
        for j in range(n-1, n-r-1, -1):
            result.append(arr[j])
    return result

llist1=LinkedList([1,2,3,4])
print(llist1)

arr1=[n for n in llist1]
print(arr1)
