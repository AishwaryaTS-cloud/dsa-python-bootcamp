# Doubly Linked List Implementation (Python)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # -----------------------------
    # INSERT AT BEGINNING (O(1))
    # -----------------------------
    def insert_start(self, data):
        new = Node(data)
        new.next = self.head

        if self.head:
            self.head.prev = new
        else:
            self.tail = new

        self.head = new

    # -----------------------------
    # INSERT AT END (O(1))
    # -----------------------------
    def insert_end(self, data):
        new = Node(data)

        if self.tail:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            self.head = self.tail = new

    # -----------------------------
    # INSERT AFTER A GIVEN NODE
    # -----------------------------
    def insert_after(self, node, data):
        if node is None:
            return

        new = Node(data)
        new.prev = node
        new.next = node.next

        if node.next:
            node.next.prev = new
        else:
            self.tail = new

        node.next = new

    # -----------------------------
    # DELETE A NODE (O(1))
    # -----------------------------
    def delete_node(self, node):
        if node is None:
            return

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    # -----------------------------
    # DISPLAY FORWARD
    # -----------------------------
    def display_forward(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    # -----------------------------
    # DISPLAY BACKWARD
    # -----------------------------
    def display_backward(self):
        curr = self.tail
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.prev
        return result


# Example
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_end(3)
    dll.insert_end(7)
    dll.insert_end(2)
    dll.insert_end(9)

    print("Forward:", dll.display_forward())
    print("Backward:", dll.display_backward())

    # delete middle node (value 7)
    node = dll.head.next
    dll.delete_node(node)

    print("After delete:", dll.display_forward())
    