class Node():
 def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.length += 1

    def __str__(self):
        current_node = self.head
        return_str = ''
        while current_node != None:
            return_str += str(current_node.data)
            current_node = current_node.next
            if current_node != None:
                return_str += ', '
        return return_str 