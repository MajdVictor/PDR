class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def middleNode(headNode):
    slowPtr = fastPtr = headNode

    while fastPtr != None and fastPtr.next != None:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return slowPtr.val


if __name__ == "__main__":

    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print(middleNode(node1))