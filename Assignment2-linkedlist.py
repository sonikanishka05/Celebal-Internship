class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index must be a positive integer (1-based).")

        if n == 1:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(n - 2):
            if temp is None or temp.next is None:
                raise IndexError("Index out of range.")
            temp = temp.next

        if temp.next is None:
            raise IndexError("Index out of range.")

        temp.next = temp.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Original List:")
    ll.print_list()

    print("\nDeleting 2nd node:")
    ll.delete_nth_node(2)
    ll.print_list()

    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete 5th node (should raise error):")
    try:
        ll.delete_nth_node(5)
    except Exception as e:
        print("Error:", e)
