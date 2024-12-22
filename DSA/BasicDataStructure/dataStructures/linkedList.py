class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head
        if temp and temp.val == value:
            self.head = temp.next
            return
        while temp:
            if temp.next and temp.next.val == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()