class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node to the end of the list."""
        if self.head is None:
            new_node = Node(data, None, None)
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        new_node = Node(data, None, itr)
        itr.next = new_node

    def print_forward(self):
        """Prints the list from head to tail."""
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        print("Forward: ", llstr)

    def print_backward(self):
        """Prints the list from tail to head using the prev reference."""
        if self.head is None:
            print("Linked list is empty")
            return

        # 1. Go to the last node
        itr = self.head
        while itr.next:
            itr = itr.next

        # 2. Iterate backwards using prev
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> " if itr.prev else str(itr.data)
            itr = itr.prev
        print("Backward: ", llstr)

# --- Testing the implementation ---
if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append("Apple")
    dll.append("Banana")
    dll.append("Cherry")
    dll.append("Date")

    dll.print_forward()
    dll.print_backward()