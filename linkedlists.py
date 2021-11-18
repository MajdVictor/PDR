class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printLinkedList(self):

        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(22)

    linkedlist = LinkedList()
    linkedlist.head = node1
    node1.next = node2
    node3.next = node3

    linkedlist.printLinkedList()

