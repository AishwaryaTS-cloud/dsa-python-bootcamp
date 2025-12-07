# Hash Table implementation using Separate Chaining

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        idx = self._hash(key)
        head = self.table[idx]

        # Update if key exists
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        # Insert new node at front
        new_node = Node(key, value)
        new_node.next = head
        self.table[idx] = new_node

    def search(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def delete(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        prev = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[idx] = curr.next
                return True
            prev = curr
            curr = curr.next

        return False


# Example usage
if __name__ == "__main__":
    ht = HashTable(5)
    ht.insert("name", "Aishwarya")
    ht.insert("age", 21)
    ht.insert("lang", "Python")

    print(ht.search("name"))
    print(ht.search("age"))

    ht.delete("age")
    print(ht.search("age"))