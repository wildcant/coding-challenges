class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Append nodes to linked list
def insertNodeAtTail(head, data):
    nnode = SinglyLinkedListNode(data)
    if head is None:
        head = nnode
        return head
    current = head
    while current.next is not None:
        current = current.next
    current.next = nnode
    return head


# Pre-append nodes to linked list
def insertNodeAtHead(head, data):
    nnode = SinglyLinkedListNode(data)
    if head is None:
        head = nnode
        return head
    nnode.next = head
    head = nnode
    return head

# Insert node at given position
def insertNodeAtPosition(head, data, position):
    if head is None:
        return head
    current = head
    nnode = SinglyLinkedListNode(data)
    for i in range(position-1):
        current = current.next
    nnode.next = current.next
    current.next = nnode
    return head


def deleteNode(head, position):
    if head is None:
        return head
    if position == 0:
        head = head.next
        return head
    current = head
    for i in range(position - 1):
        current = current.next
    current.next = current.next.next
    return head

# Print link list in reversed  orderss
def reversePrint(head):
    if (head == None):
        return  None
    reversePrint(head.next)
    print(head.data)

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)