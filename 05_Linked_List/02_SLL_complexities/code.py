# Singly Linked List Implementation to Demonstrate Operations & Their Complexities

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # ----------------------
    # ACCESS (O(n))
    # ----------------------
    def access(self, index):
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.data
            curr = curr.next
            i += 1
        return None

    # ----------------------
    # SEARCH (O(n))
    # ----------------------
    def search(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

    # ----------------------
    # INSERT AT START (O(1))
    # ----------------------
    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    # ----------------------
    # INSERT AT END (O(1) if tail exists else O(n))
    # ----------------------
    def insert_end(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    # ----------------------
    # INSERT AFTER A GIVEN NODE (O(1))
    # ----------------------
    def insert_after(self, node, value):
        if node is None:
            return
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        if node == self.tail:
            self.tail = new_node

    # ----------------------
    # DELETE START (O(1))
    # ----------------------
    def delete_start(self):
        if self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    # ----------------------
    # DELETE END (O(n) unless we store prev)
    # ----------------------
    def delete_end(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        curr.next = None
        self.tail = curr

    # ----------------------
    # DELETE AFTER A GIVEN NODE (O(1))
    # ----------------------
    def delete_after(self, node):
        if node and node.next:
            to_delete = node.next
            node.next = to_delete.next
            if to_delete == self.tail:
                self.tail = node

    # Utility: Print list
    def display(self):
        curr = self.head
        out = []
        while curr:
            out.append(curr.data)
            curr = curr.next
        return out


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_end(3)
    ll.insert_end(7)
    ll.insert_end(2)
    ll.insert_end(9)

    print("List:", ll.display())
    print("Access index 2:", ll.access(2))
    print("Search 9:", ll.search(9))

    ll.insert_start(5)
    print("After insert at start:", ll.display())

    ll.insert_end(11)
    print("After insert at end:", ll.display())

    ll.delete_start()
    print("After delete start:", ll.display())

    ll.delete_end()
    print("After delete end:", ll.display())
    second_node = ll.head.next
    ll.insert_after(second_node, 8) 
    print("After insert after second node:", ll.display())  
    ll.delete_after(second_node)
    print("After delete after second node:", ll.display())
# Note: In Python, list operations like insert and delete may have different performance